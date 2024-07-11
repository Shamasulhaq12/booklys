from django.db import models
from coresite.mixin import AbstractTimeStampModel


class Company(AbstractTimeStampModel):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE, related_name='company_owner')
    category = models.ForeignKey('assets.Categories', on_delete=models.CASCADE, related_name='company_category', null=True, blank=True)
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


class CompanyServices(AbstractTimeStampModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_services')
    service_name = models.CharField(max_length=255)
    service_description = models.TextField(null=True, blank=True)
    service_timing = models.CharField(max_length=255, null=True, blank=True)
    service_sku = models.CharField(max_length=255,unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = 'Company Service'
        verbose_name_plural = 'Company Services'


class CompanyStaff(AbstractTimeStampModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_staff')
    staff_member= models.ForeignKey('userprofile.UserProfile', on_delete=models.CASCADE, related_name='company_staff')


    class Meta:
        verbose_name = 'Company Staff'
        verbose_name_plural = 'Company Staff'


