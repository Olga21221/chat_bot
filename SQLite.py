import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('6621834838:AAFIC4QbQIAoUuCeV9Mnk9OFo5aGTzWb-n4')


@bot.message_handler(commands=['start'])
def stert(message):
    conn = sqlite3.connect("user_db.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(user_name VARCHAR(50))")

    conn.commit()

    user_list= message.text.strip()
    cur.execute("INSERT INTO users VALUES(?);", user_list)
    conn.commit()


bot.polling(none_stop=True)
