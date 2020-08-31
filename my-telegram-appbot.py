import os
import telebot


x = os.getenv("ADAFRUIT_IO_USERNAME") #ADAFRUIT_IO_USERNAME
y = os.getenv("ADAFRUIT_IO_KEY") #ADAFRUIT_IO_KEY
z = os.getenv('TELEGRAM_API_TOKEN') #telegram bot token

# Import library and create instance of REST client.
from Adafruit_IO import Client, Feed
aio = Client(x,y)

bot = telebot.TeleBot(z)

from telegram.ext import Updater,CommandHandler
import requests
chat_id ='1112488868'

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi, Would you like to turn on or off the light?(Type 'Light on' for on and 'Light off' for off)")
    bot.send_photo(chat_id, photo=("https://img.freepik.com/free-vector/flat-light-bulbs-turned-turned-off-with-light-switches_44703-329.jpg?size=626&ext=jpg"))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
  if str(message.text) == 'Light on' or str(message.text) == 'light on' or str(message.text) == 'On' or str(message.text) == 'on':
    from Adafruit_IO import Data
    data = Data(value=1)
    aio.create_data('mylightbot', data)
    bot.reply_to(message,'light is on')
    bot.send_photo(chat_id, photo=("https://ak.picdn.net/shutterstock/videos/3560576/thumb/1.jpg"))
  elif str(message.text) == 'Light off' or str(message.text) == 'light off' or str(message.text) == 'Off' or str(message.text) == 'off':
    from Adafruit_IO import Data
    data = Data(value=0)
    aio.create_data('mylightbot', data)
    bot.reply_to(message,'light is off')
    bot.send_photo(chat_id, photo=("https://ak.picdn.net/shutterstock/videos/3560594/thumb/1.jpg"))
bot.polling()

