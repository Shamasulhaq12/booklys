from django.db import models
from coresite.mixin import AbstractTimeStampModel


class SubscriptionFeature(AbstractTimeStampModel):
    feature_name = models.CharField(max_length=255)
    feature_description = models.TextField(null=True, blank=True)
    feature_status = models.BooleanField(default=True)
    subscription = models.ForeignKey('Subscription', on_delete=models.CASCADE, related_name='subscription_features', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.feature_name

    class Meta:
        verbose_name = 'Subscription Feature'
        verbose_name_plural = 'Subscription Features'


class Subscription(AbstractTimeStampModel):
    subscription_name = models.CharField(max_length=255)
    subscription_price = models.DecimalField(max_digits=10, decimal_places=2)
    subscription_duration_days = models.IntegerField(default=10)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.subscription_name

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'
