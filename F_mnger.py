import telebot
import requests
import time
from bs4 import BeautifulSoup
from telebot import types


class Currency:
    ETH_RUB = 'https://www.investing.com/crypto/currency-pairs?exchange=1029&c1=195&c2=79'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

    current_table_price = 0
    difference = 1000

    def __init__(self):
        self.current_table_price = float(self.get_currency_price().replace(',', ''))

    def get_currency_price(self):

        full_page = requests.get(self.ETH_RUB, headers=self.headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        table = soup.find('td', {'class': 'pid-1031730-last'})

        return table.text

    def check_currency(self):
        currency = float(self.get_currency_price().replace(',', ''))
        if currency >= self.current_table_price + self.difference:
            print("Курс поднялся!")
        elif currency <= self.current_table_price - self.difference:
            print("Курс опустился!")
        print("Курс Эфира сейчас: " + str(currency) + " RUB")
        #time.sleep(60)
        #self.check_currency()

    def kurs(self):
        return self.current_table_price


currency = Currency()

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
    k_ETH = str(currency.kurs())
    #if message.text == 'Курс эфира':
    bot.send_message(message.chat.id, k_ETH)


bot.polling(none_stop=True)