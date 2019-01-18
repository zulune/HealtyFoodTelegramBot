import time
import logging
import telebot

from vedis import Vedis
from config import (
    token,
    db_file,
    States
)
from keyboard import *
from inline_keyboard import *
from authenticate import *

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

bot = telebot.TeleBot(token)


def get_current_state(user_id):
    with Vedis(db_file) as db:
        try:
            return db[user_id].decode()
        except:
            return States.S_START.value


def set_state(user_id, value):
    with Vedis(db_file) as db:
        try:
            db[user_id] value
            return True
        except:
            return False


@bot.message_handler(commands=['start'])
def start(message):
    u_check = Auth.check_user(message)
    print(message)
    if u_check:
        Keyboard.start_keyboard(message)
    else:
        Auth.create_user(message)
        Keyboard.start_keyboard(message)


@bot.message_handler(regexp='Simple Keyboard')
def button_one(message):
    Keyboard.button_one_keyboard(message)


@bot.message_handler(regexp='Back to main menu')
def buck_button(message):
    Keyboard.start_keyboard(message)


@bot.message_handler(regexp='Inline keybord')
def button_programm(message):
    InlineKeyboard.button_keyboard_proggram(message)


@bot.message_handler(regexp='Callback Inline')
def callback(message):
    InlineKeyboard.callback_keyboard(message)


@bot.callback_query_handler(func=lambda c: c.data == 'callback')
def callback_answer(callback_query: types.CallbackQuery):
    bot.answer_callback_query(
        callback_query.id,
        text='Прівет, якийсь ответ.',
        show_alert=True
    )


bot.polling()
