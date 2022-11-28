import os
from dotenv import load_dotenv

import logging

from telegram import Update, ForceReply, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from google_api import detect_intent_texts


logger = logging.getLogger('support_bot')


class BotLogsHandler(logging.Handler):
    def __init__(self, telegram_token, telegram_chat_id):
        super().__init__()
        self.token = telegram_token
        self.chat_id = telegram_chat_id
        self.bot = Bot(token=self.token)

    def emit(self, record: logging.LogRecord) -> None:
        log_entry = self.format(record)
        self.bot.send_message(chat_id=self.chat_id, text=log_entry)


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Здравствуйте {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def send_telegram_message(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    user_id = update.effective_user.id
    _, msg_text = detect_intent_texts(project_id=os.environ['PROJECT_ID'], session_id=user_id, text=update.message.text, language_code='RU')
    update.message.reply_text(msg_text)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.WARNING
    )

    load_dotenv()
    token = os.environ['BOT_TOKEN']
    chat_id = os.environ['CHAT_ID']
    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(
        MessageHandler(Filters.text & ~Filters.command, send_telegram_message))

    updater.start_polling()

    updater.idle()
    bot = dispatcher.bot
    bot_logs_handler = BotLogsHandler(telegram_bot=bot, telegram_chat_id=chat_id)
    logger.addHandler(bot_logs_handler)







