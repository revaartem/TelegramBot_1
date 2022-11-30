
from flask import Flask
import telebot
import config
import os


# app = Flask(__name__)
# TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def message_start(message):
    bot.send_message(message.chat.id, 'Hello, user!')


@bot.message_handler(commands=['shelters'])
def message_start(message):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

    with open('shelters.txt') as file:
        shelters = [item.split(',') for item in file]

        for title, link in shelters:
            url_button = telebot.types.InlineKeyboardButton(text=title.strip(), url=link.strip())
            keyboard.add(url_button)

        bot.send_message(message.chat.id, 'Список укрытий', reply_markup=keyboard)


@bot.message_handler(func=lambda x: x.text.lower().startswith('слава'))
def message_text(message):
    if message.lower().startswith('слава україні'):
        bot.send_message(message.chat.id, 'Героям Слава!')
    elif message.lower().startswith('слава нації'):
        bot.send_message(message.chat.id, 'Смерть ворогам! Україна понад усе!')


bot.polling(none_stop=True)