from django.db import models
from coresite.mixin import AbstractTimeStampModel


class PayPalUserDetail(AbstractTimeStampModel):
    user = models.OneToOneField("userprofile.UserProfile", related_name='paypal_user_details', on_delete=models.CASCADE)
    paypal_email = models.EmailField(unique=True)

    def __str__(self):
        return self.paypal_email

    class Meta:
        verbose_name = 'Paypal User Detail'
        verbose_name_plural = 'Paypal User Details'


class PaymentDetails(AbstractTimeStampModel):
    user = models.ForeignKey("userprofile.UserProfile",on_delete=models.CASCADE, related_name="user_payment_intent")
    payment_id = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)
    payment_amount = models.CharField(max_length=255)
    payment_currency = models.CharField(max_length=255)
    payment_time = models.DateTimeField(auto_now_add=True)
    payment_type = models.CharField(max_length=255, null=True, blank=True)
    is_refund = models.BooleanField(default=False)
    payment_resource_id = models.CharField(max_length=255, null=True, blank=True)
    subscription = models.ForeignKey('payments_and_subscription.Subscription', on_delete=models.CASCADE, related_name='subscription_payment', null=True, blank=True)

    class Meta:
        verbose_name = 'Payment Detail'
        verbose_name_plural = 'Payment Details'
