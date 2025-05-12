from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from subscriber_utils import notify_subscribers
from datetime import datetime


@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    """ Отправка сообщения подписчикам о входе в админку """
    login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"Дата входа: {login_time}, Имя пользователя: {user.username}"
    notify_subscribers(message)