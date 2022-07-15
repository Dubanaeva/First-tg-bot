import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open("img/AnimatedSticker.tgs", 'rb')
    bot.send_sticker(message.chat.id, sti)
    sti.close()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Random number")
    item2 = types.KeyboardButton("Hello")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Welcome, {0.first_name}!\nЯ - <b>{1.first_name}</b>, ".format(message.from_user,
                                                                                                     bot.get_me()),
                    parse_mode="html", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def textcheck(message):
    if message.chat.type == "private":
        if message.text == "Random number":
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == "How are u?":
            bot.send_message(message.chat.id, 'Cool, what abut u?')
        elif message.text == "Hello":
            bot.send_message(message.chat.id, 'Bye! :)')
        else:
            bot.send_message(message.chat.id, "I dont know answer:///")


bot.polling(none_stop=True)
