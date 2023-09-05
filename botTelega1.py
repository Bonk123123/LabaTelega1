import telebot
from telebot import types
import random
# Создаем экземпляр бота
bot = telebot.TeleBot('6546602172:AAHhm30EihJyj4WC9A-KogmoufwfErPsNjQ')
# Функция, обрабатывающая команду /start


@bot.message_handler(commands=['start'])
def url(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('repository')
    btn2 = types.KeyboardButton('audio')
    btn3 = types.KeyboardButton('image')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id,
                     "repository, audio, image", reply_markup=markup)


@bot.message_handler(commands=['repository'])
def url(message):
    bot.send_message(message.from_user.id,
                     "https://github.com/Bonk123123?tab=repositories")


@bot.message_handler(commands=['image'])
def url(message):
    dlinna = random.randrange(400, 600, 10)
    shirina = random.randrange(600, 800, 10)
    bot.send_photo(message.from_user.id,
                   f'http://placekitten.com/g/{shirina}/{dlinna}')


@bot.message_handler(commands=['audio'])
def url(message):
    audio = open(r'C:/Users/Arthur/Downloads/Aerosmith_Dream_on.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)
    audio.close()


@bot.message_handler(content_types=['text'])
def url(message):
    if message.text == 'repository':
        bot.send_message(message.from_user.id,
                         "https://github.com/Bonk123123?tab=repositories")

    if message.text == 'image':
        dlinna = random.randrange(400, 600, 10)
        shirina = random.randrange(600, 800, 10)
        bot.send_photo(message.from_user.id,
                       f'http://placekitten.com/g/{shirina}/{dlinna}')

    if message.text == 'audio':
        audio = open(r'C:/Users/Arthur/Downloads/Aerosmith_Dream_on.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        audio.close()


# Запускаем бота
bot.polling(none_stop=True, interval=0)
