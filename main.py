import os
import telebot
from datetime import datetime
from dotenv import load_dotenv

from database.models import User, Item
from database.conf import session

from sqlalchemy import func

load_dotenv()

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))

def listener(messages):
    for m in messages:
        chat_id = m.chat.id
        user = session.query(User).filter(User.telegram_id==m.from_user.id).first()
        if not user:
            user = User(
                telegram_id=m.from_user.id,
                first_name=m.from_user.first_name,
                username=m.from_user.username,
            )
            session.add(user)  
        message = m.text.strip()
        if message.isdigit():
            item = session.query(Item).filter(Item.code==message).first()
            if not item:
                bot.send_message(
                    chat_id,
                    'Товара с таким номером нет'
                )
            else:
                item.views = item.views + 1
                user.views = user.views + 1 if user.views else 1
                bot.send_message(
                    chat_id,
                    f'Ссылка на товар:\n{item.link}'
                )
        else:
            bot.send_message(
                chat_id,
                'Неверный код товара'
            )
        session.commit()

bot.set_update_listener(listener)
bot.polling()