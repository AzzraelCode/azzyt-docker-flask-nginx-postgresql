import os

HELLO_MESSAGE="Привет, подписчики канала Аззраэль Коде на ТыТрубе !"
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///db/data.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False