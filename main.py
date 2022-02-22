import libb.app as app
from libb.check import check


class Parser:
    def __init__(self):
        self.app = app.app

    def run(self):
        check(app=self.app)


parser = Parser()
parser.run()
