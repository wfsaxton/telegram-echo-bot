from fastapi import FastAPI, Request
import telebot
from telebot.types import Update
from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
bot = telebot.TeleBot(TELEGRAM_TOKEN)
app = FastAPI()


@app.post(f"/{TELEGRAM_TOKEN}")
async def receive_update(request: Request):
    print(request)
    # Process update from Telegram
    update = Update.de_json(await request.json())
    bot.process_new_updates([update])
    return "!", 200


@app.get("/")
async def set_webhook():
    # Remove any existing webhook and set a new one
    bot.remove_webhook()
    bot.set_webhook(
        url=WEBHOOK_URL + "/" + TELEGRAM_TOKEN
    )  # Ensure this matches your actual ngrok URL
    return "Webhook set", 200


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)
