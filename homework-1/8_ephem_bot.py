"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import ephem

from datetime import date

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

# def planet(update, context):
#     text = update.message.text
#     split_text = text.split()
#     today = date.today()
#     if 'Mars' in split_text:
#         constell = ephem.constellation(ephem.Mars(today))
#     elif 'Jupiter' in split_text:
#         constell = ephem.constellation(ephem.Jupiter(today))
#     elif 'Venus' in split_text:
#         constell = ephem.constellation(ephem.Venus(today))
#     else:
#         constell = 'Нет данных об этой планете'
#     update.message.reply_text(constell)

def planet(update,context):
    text = update.message.text
    today = date.today()
    planet_name = text.split()[1]
    wrong_name = 'Нет данных об этой планете'
    try:
        constell = ephem.constellation(getattr(ephem,planet_name)(today))
        update.message.reply_text(constell)
    except AttributeError:
        update.message.reply_text(wrong_name)

def main():
    mybot = Updater("1331549849:AAGIXdrY9MhIuc5mFStUkanouoMKoAf_ZBc", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start",greet_user))
    dp.add_handler(CommandHandler("planet",planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
