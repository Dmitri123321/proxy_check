from libb.opening import *


def check(app):
    driver = opening(app, 'Chrome')
    url = 'https://2ip.ru'
    driver.get(url)
    input()