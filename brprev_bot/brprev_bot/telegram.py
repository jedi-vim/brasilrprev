import telebot

from brprev_bot.settings import settings


t_bot = telebot.TeleBot(settings.BOT_TOKEN)


def send_message(chat_id, payload):
    t_bot.send_message(chat_id, f'{payload}')
