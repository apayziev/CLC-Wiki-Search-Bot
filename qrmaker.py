### get linkds from telegram and send it as qrcode to user
import requests, logging, qrcode
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler
from telegram.ext.filters import Filters
from telegram.update import Update


TOKEN = '5509269318:AAFB_rA_sMQk0DCAtNHLQZrtpuGgEuanoTU'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

updater = Updater(token=TOKEN, use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to qrmaker bot!\n To get qrcode send /qrcode <link>")

def qrcode(update: Update, context: CallbackContext):
   # qrcode get link from the user and send it as qrcode to user
    link = update.message.text.split(' ')[1]
    img = qrcode.make(link) 
    update.message.reply_photo(photo=img)



dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('qrcode', qrcode))
dispatcher.add_handler(MessageHandler(Filters.all, start))

updater.start_polling()
updater.idle()