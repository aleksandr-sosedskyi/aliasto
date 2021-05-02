import datetime
import pytz

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.types import ARRAY
from sqlalchemy.orm import relationship
from database.conf import Base 


class User(Base):
    __tablename__ = 'users'
    __tableargs__ = {
        'comment' : 'Telegram users'
    }

    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable=False
    )
    telegram_id = Column(Integer, nullable=True)
    username = Column(String(50), nullable=True)
    first_name = Column(String(50), nullable=True)
    views = Column(Integer, nullable=True, default=0)
    created_at = Column(
        DateTime, 
        nullable=False,
        default=datetime.datetime.now(tz=pytz.timezone('UTC'))
    )

    def __repr__(self):
        return f"User: {self.username or ''}"


class Item(Base):
    __tablename__ = 'items'

    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable=False
    )
    code = Column(
        String(50),
        nullable=False,
        unique=True,
    )
    link = Column(
        String(100),
        nullable=False,
        unique=True,
    )
    views = Column(
        Integer,
        nullable=False,
        default=0
    )
    created_at = Column(
        DateTime, 
        nullable=False,
        default=datetime.datetime.now(tz=pytz.timezone('UTC'))
    )
