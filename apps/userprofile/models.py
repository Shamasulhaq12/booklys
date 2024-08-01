from django.db import models
from apps.core.models import User
from coresite.mixin import AbstractTimeStampModel


PROFILE_STATUS = (
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('expired', 'Expired'),
    ('suspended', 'Suspended'),
    ('deleted', 'Deleted'),
)

DESIGNATION = (
    ('employee', 'Employee'),
    ('consultant', 'Consultant'),
    ('manager', 'Manager'),
)



class UserProfile(AbstractTimeStampModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    subscription = models.ForeignKey(
        'payments_and_subscription.Subscription', on_delete=models.DO_NOTHING,
        related_name='user_subscription', null=True, blank=True)
    signature = models.CharField(max_length=255, null=True, blank=True)
    social_security_number = models.CharField(max_length=255, null=True, blank=True)
    subscription_start_date = models.DateTimeField(null=True, blank=True)
    subscription_end_date = models.DateTimeField(null=True, blank=True)
    is_payment_verified = models.BooleanField(default=False)
    calling_code = models.ForeignKey(
        'assets.CallingCodeWithName', on_delete=models.CASCADE,
        related_name='user_country_codes',
        null=True, blank=True)
    company = models.ForeignKey(
        'services.Company', on_delete=models.CASCADE, related_name='user_company', null=True, blank=True)
    designation = models.CharField(max_length=255, default='employee', choices=DESIGNATION)

    country = models.ForeignKey(
        'assets.Countries', on_delete=models.CASCADE, related_name='user_countries', null=True,
        blank=True)
    is_student = models.BooleanField(default=False)
    city = models.ForeignKey('assets.Cities', on_delete=models.CASCADE, related_name='user_cities', null=True,
                                blank=True)
    currency = models.ForeignKey('assets.Currency', on_delete=models.CASCADE, related_name='user_currency', null=True,
                                blank=True)
    timezone = models.ForeignKey('assets.CountryTimeZone', on_delete=models.CASCADE, related_name='user_timezones',
                                 null=True, blank=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    profile_status = models.CharField(max_length=255, default='inactive', choices=PROFILE_STATUS)
    work_from = models.DateTimeField(null=True, blank=True)
    price_group = models.ForeignKey('assets.PriceGroup', on_delete=models.CASCADE, related_name='user_price_group',
                                    null=True, blank=True)
    is_onsite = models.BooleanField(default=False)
    onsite_address = models.TextField(null=True, blank=True)
    online_booking_available = models.BooleanField(default=False)
    booking_interval_in_minutes = models.PositiveIntegerField(default=30)
    is_subscribed = models.BooleanField(default=False)


    def __str__(self):
        return self.first_name+' '+self.last_name

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
