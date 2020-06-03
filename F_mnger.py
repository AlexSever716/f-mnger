# - *- coding: utf- 8 - *-
import telebot
import requests
#import time
#from bs4 import BeautifulSoup
from telebot import types

def Currency():

    url = "https://api.exmo.com/v1.1/ticker"

    payload = {}
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    parse_date = response.json()
    currency = parse_date["ETH_RUB"]

    curren_ETH = round(float(currency['last_trade']), 3)

    return curren_ETH
    



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
    ETH_RUB = f"<b>{str(Currency())}</b>" + ' RUB'
    if message.text == 'Курс эфира':
        bot.send_message(message.chat.id, ETH_RUB, parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Я исполняю только жёсткие инструкции, а не ВОТ ЭТО ВОТ ВСЁ!!!")

bot.polling(none_stop=True)
