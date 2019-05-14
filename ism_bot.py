import telebot
import yaml

with open("config.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

TELEGRAM_TOKEN = cfg['TELEGRAM_TOKEN']

bot = telebot.TeleBot("TELEGRAM_TOKEN")
