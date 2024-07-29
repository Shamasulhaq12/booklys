from django.db import models
from coresite.mixin import AbstractTimeStampModel
from django.contrib.postgres.fields import ArrayField




class Company(AbstractTimeStampModel):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE, related_name='company_owner')
    address = models.TextField(null=True, blank=True)
    company_description = models.TextField(null=True, blank=True)
    about_company = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class CompanyImages(AbstractTimeStampModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_images')
    image = models.ImageField(upload_to='company_images/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.company.name

    class Meta:
        verbose_name = 'Company Image'
        verbose_name_plural = 'Company Images'


SERVICES_TYPE = (
    ('basic', 'Basic'),
    ('additional', 'additional'),
)

PRICE_TYPE = (
    ('fixed', 'Fixed'),
    ('variable', 'Variable'),
)


class Services(AbstractTimeStampModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_services')
    service_name = models.CharField(max_length=255)
    service_provider = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE, related_name='service_provider')
    service_type = models.CharField(max_length=255, choices=SERVICES_TYPE, default='basic')
    basic_service = models.ForeignKey('self', on_delete=models.CASCADE, related_name='additional_services', null=True, blank=True)
    service_description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('assets.Categories', on_delete=models.CASCADE, related_name='service_category', null=True, blank=True)
    service_timing = models.CharField(max_length=255, null=True, blank=True)
    # keywords = ArrayField(models.CharField(max_length=255), null=True, blank=True)
    is_billable = models.BooleanField(default=False)
    service_sku = models.CharField(max_length=255,unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class ServicePrice(AbstractTimeStampModel):
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='service_price')
    price = models.FloatField()
    price_type = models.CharField(max_length=255, choices=PRICE_TYPE, default='fixed')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.service.service_name

    class Meta:
        verbose_name = 'Service Price'
        verbose_name_plural = 'Service Prices'

class BookingFields(AbstractTimeStampModel):
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='service_booking_fields')
    field_name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=255)
    is_required = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.field_name

    class Meta:
        verbose_name = 'Booking Field'
        verbose_name_plural = 'Booking Fields'

class CompanyStaff(AbstractTimeStampModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_staff')
    staff_member= models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE, related_name='company_staff')


    class Meta:
        verbose_name = 'Company Staff'
        verbose_name_plural = 'Company Staff'


