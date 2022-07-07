import requests, logging
from telegram import InlineKeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler
from telegram.ext.filters import Filters
from telegram.update import Update


TOKEN = '5509269318:AAFB_rA_sMQk0DCAtNHLQZrtpuGgEuanoTU'
URL = "https://api.openweathermap.org/data/2.5/weather"
API_ID = "7089d93dd4c2f9a98fdf01559ff86e7e"


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


updater = Updater(token=TOKEN, use_context=True)

def start(update: Update, context: CallbackContext):
    update.message \
        .reply_text('Welcome to weather bot!\nTo get weather send /today <city>')

def today(update: Update, context: CallbackContext):
    message_split = update.message.text.split(' ')
    city_name = " ".join(message_split[1:])
    res = requests.get(URL, params={'q': city_name, 'appid': API_ID})
    data = res.json()
    if data["cod"] == 200:
        update.message.reply_text(
            f"Country: {data['sys']['country']}\n"
            f"City: {data['name']}\n"
            f"Description: {data['weather'][0]['description']}\n"
            f"Temperature: {data['main']['temp']} °C\n"
            f"Humidity: {data['main']['humidity']} %\n"
            f"Pressure: {data['main']['pressure']} hPa\n"
            f"Wind: {data['wind']['speed']} m/s\n"
            f"Clouds: {data['clouds']['all']} %\n"
            f"Sunrise: {data['sys']['sunrise']}\n"
            f"Sunset: {data['sys']['sunset']}\n"
        )
    else:
        update.message.reply_text("Sorry, I can't find this city")

def set_location(update: Update, context: CallbackContext):
    location_keyboard = InlineKeyboardButton(
        text='Set location',
        callback_data='set_location'
    )
    cancel_keyboard = InlineKeyboardButton(
        text='Cancel',
        callback_data='cancel'
    )
    reply_markup = ReplyKeyboardMarkup(
        [[location_keyboard, cancel_keyboard]]
    )
    update.message.reply_text(
        'Please choose an option',
        reply_markup=reply_markup
    )

    
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('today', today))
dispatcher.add_handler(CommandHandler('set_location', set_location))
dispatcher.add_handler(MessageHandler(Filters.all, start))

updater.start_polling()
updater.idle()