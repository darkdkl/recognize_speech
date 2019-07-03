
import random
import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from dialogflow_api import dialog


def get_answer(event, vk_api):
    message=dialog(event.text,event.user_id)
    bad_message='Не совсем понимаю, о чём ты.'

    if bad_message != message:
        vk_api.messages.send(
            user_id=event.user_id,
            message=message,
            random_id=random.randint(1,1000)
                            )
    
       


if __name__ == "__main__":
    vk_session = vk_api.VkApi(token=os.environ['VK_TOKEN'])
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            get_answer(event, vk_api)