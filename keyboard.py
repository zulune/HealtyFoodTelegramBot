import telebot

from telebot import types

from config import token
from authenticate import *

bot = telebot.TeleBot(token)


class Keyboard:

    @staticmethod
    def start_keyboard(message):
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        # button1 = types.KeyboardButton('\ud83d\udcbc Simple Keyboard')
        # button2 = types.KeyboardButton('\ud83c\udfe2 Inline Keyboard')
        # button3 = types.KeyboardButton('\ud83d\udcf2 Callback Inline')
        review_button = types.KeyboardButton('Залишити відгук')
        button_phone = types.KeyboardButton('Відправити номер телефону', request_contact=True)
        # markup.row(button1, button2)
        # markup.row(button3, review_button)
        markup.row(review_button, button_phone)
        bot.send_message(message.chat.id, 'Навігація: ', reply_markup=markup)

    @staticmethod
    def button_one_keyboard(message):
        markup = types.ReplyKeyboardMarkup()
        # button1 = types.KeyboardButton('Button 1')
        # button2 = types.KeyboardButton('Button 2')
        back_button = types.KeyboardButton('\ud83d\udd19 Back to main menu')
        # markup.row(button1, button2)
        markup.row(back_button)
        bot.send_message(message.chat.id, 'Keyboard level 2.', reply_markup=markup)
