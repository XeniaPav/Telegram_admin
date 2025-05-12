from subscribers.models import Subscriber
import telebot
from config.settings import API_TOKEN

bot = telebot.TeleBot(API_TOKEN)

def add_subscriber(chat_id, username=None):
    """ Добавление подписчика """
    subscriber, created = Subscriber.objects.get_or_create(user_id=chat_id, defaults={'username': username})
    return created

def notify_subscribers(message):
    """ Список всех подпичиков для отправки уведомления """
    subscribers = Subscriber.objects.all()
    for subscriber in subscribers:
        try:
            bot.send_message(subscriber.user_id, message)
        except Exception as e:
            print(f"Ошибка при отправке сообщения пользователю {subscriber.user_id}: {e}")