import os
import telegram
from telegram.ext import Updater, CommandHandler

# Hel environment variables
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bot waa shaqaynayaa!")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
