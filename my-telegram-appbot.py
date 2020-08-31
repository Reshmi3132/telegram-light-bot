import os
import telebot
!pip install adafruit-io
!pip install pyTelegramBotAPI
x = os.getenv("ADAFRUIT_IO_USERNAME") #ADAFRUIT_IO_USERNAME
y = os.getenv("ADAFRUIT_IO_KEY") #ADAFRUIT_IO_KEY
z = os.getenv('TELEGRAM_API_TOKEN') #telegram bot token

# Import library and create instance of REST client.
from Adafruit_IO import Client, Feed
aio = Client(x,y)
new = Feed(name='mylightbot')


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
 
