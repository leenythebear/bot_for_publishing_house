import logging
import os

from dotenv import load_dotenv
from telegram import ForceReply, Update
from telegram.ext import (CallbackContext, CommandHandler, Filters,
                          MessageHandler, Updater)

from google_api import detect_intent_texts
from logger import BotLogsHandler

logger = logging.getLogger("support_bot")


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        rf"Здравствуйте {user.mention_markdown_v2()}\!",
        reply_markup=ForceReply(selective=True),
    )


def send_telegram_message(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    user_id = update.effective_user.id
    _, msg_text = detect_intent_texts(
        project_id=os.environ["PROJECT_ID"],
        session_id=user_id,
        text=update.message.text,
        language_code="RU",
    )
    update.message.reply_text(msg_text)


if __name__ == "__main__":
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    tg_chat_id = os.environ["TG_CHAT_ID"]

    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    logger.setLevel(logging.INFO)
    bot_logs_handler = BotLogsHandler(
        telegram_token=tg_token, telegram_chat_id=tg_chat_id
    )
    logger.addHandler(bot_logs_handler)
    logger.info("Telegram  бот запущен")

    updater = Updater(tg_token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(
        MessageHandler(Filters.text & ~Filters.command, send_telegram_message)
    )

    updater.start_polling()

    updater.idle()
