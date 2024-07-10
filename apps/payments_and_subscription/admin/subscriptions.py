from apps.payments_and_subscription.models import Subscription
from django.contrib import admin


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscription_name', 'subscription_price', 'subscription_duration_days', 'is_active')
    list_filter = ('subscription_name', 'subscription_price', 'subscription_duration_days', 'is_active')
    search_fields = ('subscription_name', 'subscription_price', 'subscription_duration_days', 'is_active')