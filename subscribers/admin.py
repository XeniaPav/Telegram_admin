# bot/admin.py

from django.contrib import admin
from subscribers.models import Subscriber

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'subscribed_at')
    search_fields = ('user_id', 'username')