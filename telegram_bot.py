import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dialogflow_api import get_dialog
import logging
from log_to_tgm import TelegramBotLogsHandler

def with_dialogflow(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id, text=get_dialog(update.message.text, update.message.chat_id))

def main():

    logger = logging.getLogger("Logs To Telegram")
    logger.setLevel(logging.INFO)
    logger.addHandler(TelegramBotLogsHandler())
    



    try:
        updater = Updater(token=os.environ['TELEGRAM_BOT_TOKEN'])
        updater.dispatcher.add_handler(MessageHandler(Filters.text, with_dialogflow))
        updater.start_polling()
        logger.info("Telegram-Бот запущен")
    except:
        logger.critical('Проблема с Telegram-Бот', exc_info=1)



if __name__ == "__main__":
    main()
