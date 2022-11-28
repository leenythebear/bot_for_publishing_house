import logging
import os
import random
from dotenv import load_dotenv

import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType

from google_api import detect_intent_texts
from tg_bot import BotLogsHandler

logger = logging.getLogger('support_bot')


def send_vk_message(event, vk_api, project_id):
    user_id = event.user_id
    text = event.text
    is_fallback, answer_text = detect_intent_texts(project_id, user_id, text, 'RU')
    if not is_fallback:
        vk_api.messages.send(
            user_id=user_id,
            message=answer_text,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":

    load_dotenv()
    vk_token = os.environ['VK_TOKEN']

    project_id = os.environ['PROJECT_ID']

    tg_chat_id = os.environ['TG_CHAT_ID']
    tg_token = os.environ['TG_TOKEN']

    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    logger.setLevel(logging.INFO)
    bot_logs_handler = BotLogsHandler(telegram_token=tg_token,
                                      telegram_chat_id=tg_chat_id)
    logger.addHandler(bot_logs_handler)
    logger.info('VK бот запущен')
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            send_vk_message(event, vk_api, project_id)
