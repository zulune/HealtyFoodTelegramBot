import telebot
from telebot import types
from config import token

bot = telebot.TeleBot(token)


class InlineKeyboard:
    def button_two_keyboard(message):
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(
            text = 'GitHub',
            url = 'https://github.com'
        )
        keyboard.add(url_button)
        bot.send_message(message.chat.id,
            'Якщо натиснете кнопку, перейдете на сайт GitHub',
            reply_markup=keyboard)

    def callback_keyboard(message):
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(
            text='More',
            callback_data='callback'
        )
        keyboard.add(button)
        bot.send_message(message.chat.id,
            'Функція зворотнього звязку',
            reply_markup=keyboard)