from django.db import models
from coresite.mixin import AbstractTimeStampModel as AB


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
    booking_timing = models.DateTimeField()
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