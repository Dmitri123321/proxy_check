from libb.my_json import read_json
import logging
from libb.telegram import send_message as sms


def logger(name, mode='a'):
    log = logging.getLogger(name=name)
    handler = logging.FileHandler(f"log/{name}.log", mode=mode)
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    if name == 'error':
        log.setLevel(logging.ERROR)
    else:
        log.setLevel(logging.DEBUG)
    log.addHandler(handler)
    return log


class App:
    def __init__(self):
        self.sms = sms
        self.used_proxy = []
        self.config = read_json('config/config.json')
        self.log_error = logger(name='error', mode='w')
        self.log_debug = logger(name='debug', mode='w')
        self.this_is_huinya = True
        if self.config['chek_proxy']:
            pass
        else:
            with open(self.config['path_list_valid_proxy'], 'r') as f:
                self.proxy_list = [line.strip() for line in f]

app = App()
