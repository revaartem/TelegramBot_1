
from flask import Flask
import telebot
import config
import os


# app = Flask(__name__)
# TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def message_start(message):
    bot.send_message(message.chat.id, 'Вітаю. Я бот єУкриття. Якщо ти в небезпеці, хутчіш тицяй на команду списку '
                                      'укриттів та вибирай найближче!')


@bot.message_handler(commands=['shelters'])
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

        bot.send_message(message.chat.id, 'Список укриттів', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def message_text(message):
    if message.text.lower().startswith('слава нації'):
        bot.send_message(message.chat.id, 'Смерть ворогам!')

    elif message.text.lower().startswith('слава україні'):
        bot.send_message(message.chat.id, 'Героям Слава!')

    elif message.text.lower().startswith('слава'):
        bot.send_message(message.chat.id, 'Україні!')

    elif message.text.lower().startswith('героям'):
        bot.send_message(message.chat.id, 'Слава!')

    elif message.text.lower().startswith('україна'):
        bot.send_message(message.chat.id, 'Понад усе!')

    elif message.text.lower().startswith('руский') or\
         message.text.lower().startswith('русский') or\
         message.text.lower().startswith('рускій') or\
         message.text.lower().startswith('русскій'):
        bot.send_message(message.chat.id, 'Иди нахуй!')

    elif message.text.lower().startswith('путин') or\
         message.text.lower().startswith('путін'):
        bot.send_message(message.chat.id, 'Хуйло!')
    else:
        bot.send_message(message.chat.id, 'Пробач, не розумію тебе. Спробуй ще раз.')



bot.polling(none_stop=True)