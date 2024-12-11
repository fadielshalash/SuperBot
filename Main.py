import os
import random
from flask import Flask, request
import telebot

API_KEY = "7794504006:AAHoVFCmvsuGSLW32VdKfm9savQDmoruMIc"
WEBHOOK_URL = "https://c0cc-77-137-43-45.ngrok-free.app//webhook"


bot = telebot.TeleBot(API_KEY)
app = Flask(__name__)
@app.route('/sanity')
def sanity():return "Server is running"
@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data(as_text=True)
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'OK', 200
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello, I am a Telegram bot developed by Fadi Shalash :) . Use /help to see what I can do for you.")
    image_path = os.path.join(os.getcwd(), "welcome_image.jpg")
    with open(image_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)



@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "I support the following commands: \n /start \n /info \n /help \n /status \n /quote \n /links  ")

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "I am a simple Telegram bot. I'm here to help you. \n My Developer is Fadi Shalash \n fadielshalash@gmail.com \n https://www.linkedin.com/in/fadi-shalash-944b6628a/.")
    image_path = os.path.join(os.getcwd(), "me.jpeg")
    with open(image_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo,protect_content=True)
    

@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "I am up and running, \n I am ready to help you.\n Already Working to develop more features in the future.")
@bot.message_handler(commands=['quote'])
def status(message):
    with open('quotes.txt', 'r') as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes)
        bot.reply_to(message, f"Quote of the day:\n {random_quote}")
@bot.message_handler(commands=['links'])
def status(message):
    bot.reply_to(message, "ALl the links:\n https://www.google.com \n https://www.facebook.com \n https://www.instagram.com")

# Start Flask server
if __name__ == "__main__":
    # Set webhook
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    app.run(port=8080)
