from django.db import models


class Subscription(models.Model):
    subscription_name = models.CharField(max_length=255)
    subscription_price = models.DecimalField(max_digits=10, decimal_places=2)
    subscription_duration_days = models.IntegerField(default=10)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.subscription_name

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'

