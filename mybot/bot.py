import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings
import ephem
from datetime import date

logging.basicConfig(filename = "bot.log", level = logging.INFO)

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Привет!")

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def planet(update, context):
    text = update.message.text
    split_text = text.split()
    today = date.today()
    if 'Mars' in split_text:
        constell = ephem.constellation(ephem.Mars(today))
    elif 'Jupiter' in split_text:
        constell = ephem.constellation(ephem.Jupiter(today))
    elif 'Venus' in split_text:
        constell = ephem.constellation(ephem.Venus(today))
    else:
        constell = 'Нет данных об этой планете'
    update.message.reply_text(constell)

def main():
    mybot = Updater(settings.API_KEY, 
        use_context = True, request_kwargs = PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start",greet_user))
    dp.add_handler(CommandHandler("planet",planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()