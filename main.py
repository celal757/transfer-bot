# -*- coding: utf-8 -*-
from flask import Flask
from threading import Thread
import asyncio
from aiogram import Bot, Dispatcher, types
import logging

# -------------------- ТВОЙ ТОКЕН --------------------
BOT_TOKEN = "8253524202:AAGrtHT-KlM7fp2f3Ebzz1_kkucjrAMRGP0"

# -------------------- Flask для Render --------------------
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Бот работает!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    thread = Thread(target=run_flask)
    thread.start()

# -------------------- Telegram бот --------------------
logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    user = message.from_user.first_name or "друг"
    await message.answer(f"Привет, {user}! 👋 Ты написал: {message.text}")

# -------------------- Запуск --------------------
async def main():
    keep_alive()  # Flask сервер для Render
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
