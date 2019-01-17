import telebot
import requests

from config import token

bot = telebot.TeleBot(token)


class Auth:

    def create_user(message):
        url = 'http://localhost:8000/api/v2/user'
        req = requests.get(url)
        print(req)