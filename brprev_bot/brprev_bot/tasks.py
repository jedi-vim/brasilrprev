from celery import Celery

from brprev_bot.database import db
from brprev_bot.settings import settings
from brprev_bot.models import Chat
from brprev_bot.telegram import send_message, t_bot
from brprev_bot.decorators import flask_context

app = Celery(__name__, broker=f'redis://guest@{settings.REDIS_HOST}/1')

app.conf.beat_schedule = {
    "look_for_new_telegram_chats": {
        "task": "brprev_bot.tasks.look_for_new_telegram_chats",
        "schedule": 10.0
    }
}


@app.task(max_retries=5, default_retry_delay=5)
@flask_context
def look_for_new_telegram_chats():
    updates = t_bot.get_updates(timeout=2)
    for update in updates:
        message = update.message.json
        if message['text'] == '/start':
            chat_info = message['chat']
            greeting_name = f'{chat_info.get("first_name")} {chat_info.get("last_name")}'
            db.session.add(Chat(greeting_name=greeting_name, telegram_id=chat_info['id']))
    db.session.commit()


@app.task(max_retries=10, default_retry_delay=5)
@flask_context
def broadcast_search_result(payload):
    for chat in Chat.query.all():
        send_message(chat.telegram_id, f'{payload}')
