import telegram
from emoji import emojize

from st2common.runners.base_action import Action


class TelegramSendMessageAction(Action):
    def run(self, message, chat_id):
        bot = telegram.Bot(token=self.config['apikey'])
        m = bot.sendMessage(text=emojize(message, use_aliases=True),
                            chat_id=chat_id,
                            parse_mode=telegram.ParseMode.HTML,
                            disable_web_page_preview=True)
        return m
