#!/usr/bin/env python
import telebot
import random
from telebot import types
token = '1469789335:AAHtRcVSuRvphCppLp57jD14kUY-uUhG99o'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Дарова, готов ебасосить Андрея?")
    bot.send_message(message.chat.id, "/start \n/buttons")
    # Команда buttons
@bot.message_handler(commands=["buttons"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Сливы Андрея")
        item2=types.KeyboardButton("Сливы Юры")
        item3=types.KeyboardButton("Сливы Богдана")
        item4=types.KeyboardButton("Выход")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        bot.send_message(m.chat.id, 'Выбирай ',  reply_markup=markup)




@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Очисти чат':
        i = 0
        while i < 15:
            bot.send_message(message.chat.id, 'Андрей саси')
            i += 1
        bot.send_message(message.chat.id, 'Чат очищен)')
    elif message.text == 'Скики у мене члэн?':
        a = random.randint(1, 15)
        bot.send_message(message.chat.id, a)
    elif message.text == 'Ладно я спатки':
        bot.send_message(message.chat.id, 'Пошёл нахуй')
    elif message.text == 'да':
        bot.send_message(message.chat.id, 'Пизда')
    elif message.text == 'Да':
        bot.send_message(message.chat.id, 'Пизда')
    elif message.text == '(':
        bot.send_message(message.chat.id, 'Кто грустит тот трансвестит')
    elif message.text == ')':
        bot.send_message(message.chat.id, 'Хули лыбимся?')
    elif message.text.strip() == 'Сливы Андрея' :
        bot.send_message(message.chat.id, 'Хуй соси')
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'Сливы Юры':
        bot.send_message(message.chat.id, 'Хуй соси')
    elif message.text.strip() == 'Сливы Богдана':
        bot.send_message(message.chat.id, 'Хуй соси')
    elif message.text.strip() == 'Выход':
        bot.send_message(message.chat.id, 'Куда ты выйдешь, добоёб?')


# Запускаем бота
bot.polling(none_stop=True, interval=0)

