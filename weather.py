import telebot

bot = telebot.TeleBot('6621834838:AAFIC4QbQIAoUuCeV9Mnk9OFo5aGTzWb-n4')

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть. Напиши название города.)')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    sity = message.text.strip().lower()


bot.polling()