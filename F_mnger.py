# - *- coding: utf- 8 - *-
import telebot
import requests
#import time
#from bs4 import BeautifulSoup
from telebot import types

def Currency():

    #ETH_RUB = 'https://www.investing.com/crypto/currency-pairs?exchange=1029&c1=195&c2=79'
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}


    url = "https://api.exmo.com/v1.1/ticker"

    payload = {}
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    parse_date = response.json()
    currency = parse_date["ETH_RUB"]

    curren_ETH = currency['last_trade']

    return curren_ETH
    #print(currency['last_trade'])



bot = telebot.TeleBot("1180230199:AAGO1Qyqc_aKD4BSbusz8IgpYB7OvgrmYmg")

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Курс эфира")
    markup.add(btn1)

    send_mess = f"<b>Привет {message.from_user.first_name}!</b>,\n ты написал мне /start"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def ETH_messages(message):
    k_ETH = str(Currency())
    #if message.text == 'Курс эфира':
    bot.send_message(message.chat.id, k_ETH)

bot.polling(none_stop=True)
