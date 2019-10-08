import telebot

from telebot import types

from config import token
from authenticate import *

bot = telebot.TeleBot(token)


class Keyboard:
    def start_keyboard(message):
        markup = types.ReplyKeyboardMarkup()
        # button1 = types.KeyboardButton('\ud83d\udcbc Simple Keyboard')
        # button2 = types.KeyboardButton('\ud83c\udfe2 Inline Keyboard')
        # button3 = types.KeyboardButton('\ud83d\udcf2 Callback Inline')
        review_button = types.KeyboardButton('Оставить отзыв')
        # markup.row(button1, button2)
        markup.row(button3, review_button)
        bot.send_message(message.chat.id, 'Моє меню: ', reply_markup=markup)

    def button_one_keyboard(message):
        markup = types.ReplyKeyboardMarkup()
        # button1 = types.KeyboardButton('Button 1')
        # button2 = types.KeyboardButton('Button 2')
        back_button = types.KeyboardButton('\ud83d\udd19 Back to main menu')
        # markup.row(button1, button2)
        markup.row(back_button)
        bot.send_message(message.chat.id, 'Keyboard level 2.', reply_markup=markup)