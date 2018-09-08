from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import api_token

#Логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

API_KEY = api_token.API_KEY #Подключаем свой API токен через файл

def greet_user(bot, update): #Отдаем сообщение
    text = 'Вызван старт /start'
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = 'Привет {}! Ты написал: {}'.format(update.message.chat.first_name, update.message.text)
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username,
                                                       update.message.chat.id,
                                                       update.message.text)
    update.message.reply_text(user_text)

def main ():
    mybot = Updater(API_KEY) #Для работы через проксю нужно добавить request_kwargs=PROXY
    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    mybot.start_polling()# Проверяем новые сообщения
    mybot.idle()# Работает пока пренудительно не остановим (циклично)

main()
