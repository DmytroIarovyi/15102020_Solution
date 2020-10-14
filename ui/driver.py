from selenium import webdriver

from config import config
from ui.singleton import Singleton


class Driver(object):
    __metaclass__ = Singleton
    chrome = webdriver.Chrome(config['DRIVER']['PATH'])
    chrome.maximize_window()
    chrome.get(config['APP']['HOME_URL'])
