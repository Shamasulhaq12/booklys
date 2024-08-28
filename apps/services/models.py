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
STAFF_DESIGNATION = (
    ('employee', 'Employee'),
    ('consultant', 'Consultant'),
    ('manager', 'Manager'),
)


class CompanyStaff(AbstractTimeStampModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_staff')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nick_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    designation = models.CharField(max_length=255, choices=STAFF_DESIGNATION, default='employee')
    image = models.ImageField(upload_to='staff_images/', null=True, blank=True)
    signature = models.CharField(max_length=255, null=True, blank=True)
    social_security_number = models.CharField(max_length=255, null=True, blank=True)
    price_group = models.ForeignKey('assets.PriceGroup', on_delete=models.CASCADE, related_name='user_price_group',
                                    null=True, blank=True)
    calling_code = models.ForeignKey('assets.CallingCodeWithName', on_delete=models.CASCADE, related_name='staff_country_codes', null=True, blank=True)
    is_student = models.BooleanField(default=False)
    work_from = models.DateTimeField(null=True, blank=True)
    is_onsite = models.BooleanField(default=False)
    booking_interval_in_minutes = models.PositiveIntegerField(default=30)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Company Staff'
        verbose_name_plural = 'Company Staff'


class ContactInformation(AbstractTimeStampModel):

    staff = models.ForeignKey(CompanyStaff, on_delete=models.CASCADE, related_name='staff_contacts')
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.staff.first_name

    class Meta:
        verbose_name = 'Contact Information'
        verbose_name_plural = 'Contact Information'




class Services(AbstractTimeStampModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_services')
    service_name = models.CharField(max_length=255)
    service_providers = models.ManyToManyField(CompanyStaff, related_name='service_providers')
    service_type = models.CharField(max_length=255, choices=SERVICES_TYPE, default='basic')
    basic_service = models.ForeignKey('self', on_delete=models.CASCADE, related_name='additional_services', null=True, blank=True)
    service_description = models.TextField(null=True, blank=True)
    is_free = models.BooleanField(default=False)
    price_type = models.CharField(max_length=255, choices=PRICE_TYPE, default='fixed')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
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



DAY_CHOICES = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)
class WorkSchedule(AbstractTimeStampModel):
    staff = models.ForeignKey(CompanyStaff, on_delete=models.CASCADE, related_name='staff_schedule')
    day = models.CharField(max_length=255, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_break_time = models.TimeField(null=True, blank=True)
    end_break_time = models.TimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.staff.first_name

    class Meta:
        verbose_name = 'Work Schedule'
        verbose_name_plural = 'Work Schedules'