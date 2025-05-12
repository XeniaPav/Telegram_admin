import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from subscriber_utils import bot, add_subscriber

def register_handlers():
    @bot.message_handler(commands=['start'])
    def start(message):
        chat_id = message.chat.id
        username = message.chat.username
        if add_subscriber(chat_id, username):
            bot.send_message(chat_id, "Вы подписаны на рассылку!")
        else:
            bot.send_message(chat_id, "Вы уже подписаны на рассылку.")

if __name__ == "__main__":
    register_handlers()
    bot.polling(none_stop=True)