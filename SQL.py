import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('6621834838:AAFIC4QbQIAoUuCeV9Mnk9OFo5aGTzWb-n4')


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('tad.sql')  # команда создания БД
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name_user varchar(50), pass varchar(50))')
    conn.commit()  # добавить таблицу в базу данных
    cur.close()  # закрываем курсор
    conn.close()  # закрываем соединение

    bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрируем! Введи свое имя')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    name = message.text.strip()
    conn = sqlite3.connect('tad.sql')  # команда создания БД
    cur = conn.cursor()
    people_name = message.text.strip()
    cur.execute(f"SELECT name_user FROM users WHERE name_user = {people_name}")
    data = cur.fetchone()
    if data in None:
        name = message.text.strip()
        cur.execute("INSERT INTO users(name_user, pass) VALUES(name)")
        conn.commit()
    else:
        bot.send_message('Такой пользователь уже зарегистрирован')
    bot.send_message(message.chat.id, 'Введите пароль ')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    psw = message.text.strip()

    conn = sqlite3.connect('tad.sql')  # команда создания БД
    cur = conn.cursor()
    cur.execute("INSERT INTO users(pass) VALUES(psw)")
    conn.commit()  # добавить таблицу в базу данных
    cur.close()  # закрываем курсор
    conn.close()  # закрываем соединение

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Список пользователей.', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callbeck(call):
    conn = sqlite3.connect('tad.sql')  # команда создания БД
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()  # возвращает все найденые записи

    info = ''
    for el in users:
        info += f'Имя: {el[1]} пароль: {el[2]}\n'
    bot.send_message(call.message.chat.id, info)


bot.polling(none_stop=True)
