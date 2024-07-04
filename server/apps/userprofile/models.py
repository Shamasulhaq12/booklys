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

class UserProfile(AbstractTimeStampModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    subscription = models.ForeignKey(
        'payments_and_subscription.Subscription', on_delete=models.DO_NOTHING,
        related_name='user_subscription', null=True, blank=True)
    subscription_start_date = models.DateField(null=True, blank=True)
    subscription_end_date = models.DateField(null=True, blank=True)
    calling_code = models.ForeignKey(
        'assets.CallingCodeWithName', on_delete=models.CASCADE,
        related_name='user_country_codes',
        null=True, blank=True)
    country = models.ForeignKey(
        'assets.Countries', on_delete=models.CASCADE, related_name='user_countries', null=True,
        blank=True)
    city = models.ForeignKey('assets.Cities', on_delete=models.CASCADE, related_name='user_cities', null=True,
                                blank=True)
    currency = models.ForeignKey('assets.Currency', on_delete=models.CASCADE, related_name='user_currency', null=True,
                                blank=True)
    timezone = models.ForeignKey('assets.CountryTimeZone', on_delete=models.CASCADE, related_name='user_timezones',
                                 null=True, blank=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    profile_status = models.CharField(max_length=255, default='inactive', choices=PROFILE_STATUS)


    def __str__(self):
        return self.first_name+' '+self.last_name

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
