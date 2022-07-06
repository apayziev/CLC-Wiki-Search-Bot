from telegram.bot import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

updater = Updater(token=settings.TELEGRAM_TOKEN, use_context=True)

def start(update, context):
    update.message.reply_text("Hello World!")


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
