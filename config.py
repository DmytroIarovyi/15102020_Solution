import configparser
import os

os.chdir(os.path.join(os.path.abspath('../..'), 'configs'))

config = configparser.ConfigParser()
config.read("config.ini")

