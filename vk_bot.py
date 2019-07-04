import random
import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from dialogflow_api import get_dialog
import logging
from log_to_tgm import TelegramBotLogsHandler


def get_answer(event, vk_api):
    message = get_dialog(event.text, event.user_id)

    bad_message = 'Не совсем понимаю, о чём ты.'

    if bad_message != message:
        vk_api.messages.send(
            user_id=event.user_id,
            message=message,
            random_id=random.randint(1, 1000)
        )


def main(vk_api=vk_api):
    logger = logging.getLogger("Logs To Telegram")
    logger.setLevel(logging.INFO)
    logger.addHandler(TelegramBotLogsHandler())

    try:

        vk_session = vk_api.VkApi(token=os.environ['VK_TOKEN'])
        vk_api = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)
        logger.info("VK-Бот запущен")
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                get_answer(event, vk_api)

    except:
        logger.critical('Проблема с VK-Бот', exc_info=1)


if __name__ == "__main__":
    main()
