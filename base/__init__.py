import telebot

bot = telebot.TeleBot('6757514713:AAFbwHmv4BZMHHtqkf9WBA2YsDNEUbsHHgc')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, message)

@bot.message_handler(commands=['main'])
def main(message):
    bot.send_message(message.chat.id, f'Игрок {message.from_user.first_name} '
                                      f'{message.from_user.last_name}')

@bot.message_handler()  #Этот метод должен обрабатываться снизу
def info(message):

    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'{"Таможня"}')
bot.polling(non_stop=True)















# def start():
#     return 'Start'
#
# if __name__ == '__main__':
#     print(start())