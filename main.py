import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('6621834838:AAFIC4QbQIAoUuCeV9Mnk9OFo5aGTzWb-n4')


# Постоянные кнопки в боте
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('website')
    btn2 = types.KeyboardButton('youtube')
    markup.row(btn1)
    markup.row(btn2)
    bot.send_message(message.chat.id, 'Hello', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


# Выполнения действий для постоянных конопок
def on_click(message):
    if message.text == 'website':
        bot.send_message(message.chat.id, 'website')
    elif message.text == 'youtube':
        bot.send_message(message.chat.id, 'youtube')
    bot.register_next_step_handler(message, on_click)


# Команда /start
@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет, скучаешь?)')


# Команда /name. Выводит Имя Фамилию и id пользователя
@bot.message_handler(commands=['name'])
def name(message):
    bot.send_message(message.chat.id,
                     f'{message.from_user.first_name} {message.from_user.last_name}, {message.from_user.id}')


# Принимает на вход текст. UPD пока что да и нет(рус и англ)
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text.lower() == 'да' or message.text.lower() == 'yes':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Тогда перейди по ссылке', url='https://rt.pornhub.com/'))
        bot.send_message(message.chat.id, 'Тогда перейди по ссылке', reply_markup=markup)
    elif message.text.lower() == 'нет' or message.text.lower() == 'no':
        bot.send_message(message.chat.id, 'Тогда занимайся своими делами дальше')
    else:
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton('Но можешь нажать сюда', url='https://www.youtube.com/watch?v=IkCh8VfN2d4'))
        bot.send_message(message.chat.id, 'Я не знаю что на это ответить', reply_markup=markup)


# Принимает на вход фото
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://google.com')
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, 'Красивое фото', reply_markup=markup)


# Кнопки которые относятся к действиям с фото
@bot.callback_query_handler(func=lambda callbeck: True)
def callback_msg(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
        bot.edit_message_text('Зачем удалил?', callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'edit':
        bot.edit_message_text('Ничего менять не буду', callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop=True)
