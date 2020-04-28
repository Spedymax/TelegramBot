import telebot

bot = telebot.TeleBot('1132273630:AAGw9u48Q43OApq1CfVK5DplQtTtgADojlo')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Дарова, готов ебасосить олю?")


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Очисти чат':
        i = 0
        while i < 25:
            bot.send_message(message.chat.id, 'Оля саси')
            i += 1
        bot.send_message(message.chat.id, 'Чат очищен)')




bot.polling()
