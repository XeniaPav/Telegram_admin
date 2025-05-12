from django.db import models

class Subscriber(models.Model):
    """ Модель подписки """
    user_id = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="ID пользователя"
    )
    username = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name = "Имя пользователя (если доступно)"
    )
    subscribed_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время подписки"
    )

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"