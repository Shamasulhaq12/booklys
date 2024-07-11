from django.db import models
from coresite.mixin import AbstractTimeStampModel


class Categories(AbstractTimeStampModel):
    index = models.PositiveBigIntegerField(default=0)
    name = models.CharField(max_length=100, unique=True, error_messages={
                            'unique': "This Category has already been registered."})
    category_slug = models.SlugField(max_length=100, unique=True)
    image = models.FileField(upload_to='category', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        db_table = 'categories'


