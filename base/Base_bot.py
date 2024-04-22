import telebot
from telebot import types

bot = telebot.TeleBot('6757514713:AAFbwHmv4BZMHHtqkf9WBA2YsDNEUbsHHgc')

@bot.message_handler(commands=['start'])
def main(message):

    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Выбор игры')
    btn2 = types.KeyboardButton('Статистика')
    brn3 = types.KeyboardButton('Стоп')
    murkup.row(btn1, btn2, brn3)
    bot.send_message(message.chat.id, f'Hello {message.chat.first_name}. Я начал свою работу', reply_markup=murkup)
@bot.message_handler(commands=['main'])
def main(message):
    bot.send_message(message.chat.id, f'Игрок {message.from_user.first_name} '
                                      f'{message.from_user.last_name}')

@bot.message_handler()  #Этот метод должен обрабатываться снизу
def info(message):

    if message.text.lower() == 'привет':
        bot.reply_to(message, f'{"Таможня"}')
bot.polling(non_stop=True)