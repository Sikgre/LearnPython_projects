import logging
from datetime import date
from random import randint
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings
# import ephem

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

def guess_number(update, context):
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_number(user_number)
        except (TypeError, ValueError):
            message = 'Введите целое число'
    else:
        message = 'Не играем'
    update.message.reply_text(message)

def play_random_number(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        result = f'Твоё число {user_number} больше моего {bot_number}, ты выиграл!'
    elif user_number == bot_number:
        result = f'Твоё число {user_number} равно моему {bot_number}, ничья!' 
    else:
        result = f'Моё число {bot_number} больше твоего {user_number}, я выиграл!'
    return result


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

def main():
    mybot = Updater(settings.API_KEY, 
        use_context = True, request_kwargs = PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start",greet_user))
    dp.add_handler(CommandHandler("guess",guess_number))
    # dp.add_handler(CommandHandler("planet",planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    
    logging.info('Бот стартовал')
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()