from django.db import models
from coresite.mixin import AbstractTimeStampModel


class Categories(AbstractTimeStampModel):
    index = models.PositiveBigIntegerField(default=0)
    name = models.CharField(max_length=100, unique=True, error_messages={
                            'unique': "This Category has already been registered."})
    category_slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=256)
    image = models.FileField(upload_to='category', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        db_table = 'categories'


class PriceGroup(AbstractTimeStampModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Price Group'
        verbose_name_plural = 'Price Groups'
        db_table = 'price_group'
