from sqlalchemy import Column, Integer, String

from brprev_bot.database import db


class Chat(db.Model):
    __tablename__ = 'chat'

    id = Column(Integer, primary_key=True)
    greeting_name = Column(String(30), nullable=False)
    telegram_id = Column(String(10), nullable=False)

    def __str__(self):
        print(f'Chat ID={self.id}[greeting_name={self.greeting_name}, t_id={self.telegram_id}]')
