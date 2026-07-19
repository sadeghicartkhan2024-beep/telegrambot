from telegram.ext import Updater, CommandHandler

import os

TOKEN = os.environ["TOKEN"]

def start(update, context):
    update.message.reply_text(
        """سلام 👋

به ربات شرکت نگین تمدن پاسارگاد خوش آمدید.

1- معرفی شرکت
2- محصولات
3- استعلام قیمت
4- ارتباط با کارشناس
5- آدرس شرکت
"""
    )

updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

print("Bot Started...")

updater.start_polling()
updater.idle()
