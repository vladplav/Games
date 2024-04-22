import telebot

bot = telebot.TeleBot('6757514713:AAFbwHmv4BZMHHtqkf9WBA2YsDNEUbsHHgc')

@bot.message_handler(commands=[
    'start',
    'main',
    'help'
])
def main(message):
    bot.send_message(message.chat.id, message)


bot.polling(non_stop=True)















# def start():
#     return 'Start'
#
# if __name__ == '__main__':
#     print(start())