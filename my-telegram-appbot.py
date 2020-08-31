import os
!pip install adafruit-io
!pip install python-telegram-bot
!pip install pyTelegramBotAPI
x = os.getenv("ADAFRUIT_IO_USERNAME") #ADAFRUIT_IO_USERNAME
y = os.getenv("ADAFRUIT_IO_KEY") #ADAFRUIT_IO_KEY
from Adafruit_IO import Client, Feed
aio = Client(x,y)
# Create Feed object with name 'mylightbot'.
new = Feed(name='mylightbot')
import telebot
bot = telebot.TeleBot(z)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi, Tell your command")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
  if str(message.text) == 'Light on':
    from Adafruit_IO import Data
    data = Data(value=1)
    aio.create_data('mylightbot', data)
    bot.reply_to(message,'light is on')
  elif str(message.text) =='Light off':
    from Adafruit_IO import Data
    data = Data(value=0)
    aio.create_data('mylightbot', data)
    bot.reply_to(message,'light is off')
bot.polling()
