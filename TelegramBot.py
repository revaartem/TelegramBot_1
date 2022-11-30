
from flask import Flask
import telebot
import config
import os


# app = Flask(__name__)
# TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(config.token)


# @bot.message_handler(commands=['start'])
# def message_start(message):
#     bot.send_message(message.chat.id, 'Hello, user!')


@bot.message_handler(commands=['start'])
def message_start(message):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)

    with open('shelters.txt') as file:
        shelters = [item.split(',') for item in file]
        # shelters = [item for item in file]
        # print(shelters)
        for source in shelters:
            # for title, link in source:
            url_button = telebot.types.InlineKeyboardButton(text=source[0].strip(), url=source[1].strip())
            keyboard.add(url_button)

        bot.send_message(message.chat.id, 'Список укрытий', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def message_text(message):
    if message.lower().startswith('слава україні'):
        bot.send_message(message.chat.id, 'Героям Слава!')
    elif message.lower().startswith('слава нації'):
        bot.send_message(message.chat.id, 'Смерть ворогам! Україна понад усе!')


bot.polling(none_stop=True)