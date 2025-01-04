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
    mobile = models.CharField(max_length=255, null=True, blank=True)
    family = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    other_info = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length=255, null=True, blank=True)
    personal_number = models.CharField(max_length=255, null=True, blank=True)
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
    is_subscribed = models.BooleanField(default=False)


    def __str__(self):
        return self.first_name+' '+self.last_name

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

class PatientFiles(AbstractTimeStampModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='patient_files')
    file = models.FileField(upload_to='patient_files/')
    file_type = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name+' '+self.user.last_name

    class Meta:
        verbose_name = 'Patient File'
        verbose_name_plural = 'Patient Files'