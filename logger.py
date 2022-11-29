import logging

from telegram import Bot


class BotLogsHandler(logging.Handler):
    def __init__(self, telegram_token, telegram_chat_id):
        super().__init__()
        self.token = telegram_token
        self.chat_id = telegram_chat_id
        self.bot = Bot(token=self.token)

    def emit(self, record: logging.LogRecord) -> None:
        log_entry = self.format(record)
        self.bot.send_message(chat_id=self.chat_id, text=log_entry)
