import telebot
import requests

from config import token


bot = telebot.TeleBot(token)


class Review:

    def get_review(message):
        url = 'http://localhost:8000/api/review'