import os
import random
from dotenv import load_dotenv

import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType

from google_api import detect_intent_texts


def echo(user_id, text, vk_api):
    vk_api.messages.send(
        user_id=user_id,
        message=text,
        random_id=random.randint(1, 1000)
    )


if __name__ == "__main__":
    load_dotenv()
    vk_token = os.environ['VK_TOKEN']
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            message = event.message
            user_id = event.user_id
            is_fallback, msg_text = detect_intent_texts(project_id=project_id,
                                           session_id=user_id,
                                           text=message,
                                           language_code='RU')
            if not is_fallback:
                echo(user_id, msg_text, vk_api)


