from django.db import models
from coresite.mixin import AbstractTimeStampModel as AB
from django.core.validators import MinValueValidator, MaxValueValidator


BOOKINGSTATUS=(
    ('Pending', 'Pending'),
    ('Confirmed', 'Confirmed'),
    ('Cancelled', 'Cancelled'),
    ('Completed', 'Completed'),
)
PAYMENT_TYPE=(
    ("on_the_spot", "On The Spot"),
    ("card_payment", "Card Payment"),
    ("online_payment", "Online Payment"),
    ("wallet_payment", "Wallet Payment"),
    ("other", "Other"),
)


class Bookings(AB):
    service = models.ForeignKey('services.Services', on_delete=models.CASCADE, related_name='service_bookings')
    email = models.EmailField(blank=True, null=True)
    user = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE, related_name='client_profile', null=True, blank=True)
    booking_date = models.DateField()
    start_booking_slot = models.DateTimeField(null=True, blank=True)
    end_booking_slot = models.DateTimeField(null=True, blank=True)
    phone= models.CharField(max_length=20, null=True, blank=True)
    booking_description = models.TextField(null=True, blank=True)
    booking_status = models.CharField(max_length=255, choices=BOOKINGSTATUS, default='Pending')
    payment_type = models.CharField(max_length=255, choices=PAYMENT_TYPE, default='on_the_spot')
    is_active = models.BooleanField(default=True)
    payment_status = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        db_table = 'bookings'
        ordering = ['-id']
        indexes = [
            models.Index(fields=['-id']),
            models.Index(fields=['-created_at']),
        ]


class ClientFeedback(AB):
    booking = models.ForeignKey(Bookings, on_delete=models.CASCADE, related_name='booking_feedback')
    rating = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE, related_name='client_feedback')
    feedback = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Client Feedback'
        verbose_name_plural = 'Client Feedback'
        db_table = 'client_feedback'
        ordering = ['-id']
        indexes = [
            models.Index(fields=['-id']),
            models.Index(fields=['-created_at']),
        ]

class ServiceFeedback(AB):
    service = models.ForeignKey('services.Company', on_delete=models.CASCADE, related_name='company_feedback')
    rating = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    feedback = models.TextField()
    user = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE, related_name='service_feedback')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Service Feedback'
        verbose_name_plural = 'Service Feedback'
        db_table = 'service_feedback'
        ordering = ['-id']
        indexes = [
            models.Index(fields=['-id']),
            models.Index(fields=['-created_at']),
        ]


class Journals(AB):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    user = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE, related_name='journal_user', null=True, blank=True)
    owner = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE, related_name='journal_owner', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(null=True, blank=True)


    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'
        db_table = 'journals'
        ordering = ['-id']
        indexes = [
            models.Index(fields=['-id']),
            models.Index(fields=['-created_at']),
        ]
