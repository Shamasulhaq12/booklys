from django.db import models
from coresite.mixin import AbstractTimeStampModel

TEMPLATE_TYPES =[
    ('text', 'text'),
    ('phrase', 'phrase'),
    ('drawing', 'drawing'),
    ('image', 'image'),
    ('marker', 'marker'),
]

class Templates(AbstractTimeStampModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    shortcut = models.CharField(max_length=255, null=True, blank=True)
    kva_code = models.ManyToManyField('booking.KVACodes', related_name='templates', blank=True)
    diagnosis = models.ManyToManyField('booking.Diagnosis', related_name='templates', blank=True)
    contact_case = models.CharField(max_length=255, null=True, blank=True)
    assessment = models.TextField(null=True, blank=True)
    action = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='templates/images/', null=True, blank=True)
    template_type = models.CharField(max_length=255, choices=TEMPLATE_TYPES, default='text')


    class Meta:
        verbose_name_plural = 'Templates'
        db_table = 'templates'


class Forms(AbstractTimeStampModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    valid_time_in_days = models.IntegerField(null=True, blank=True)
    form_title = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    surename = models.CharField(max_length=255, null=True, blank=True)
    personal_number = models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Forms'
        db_table = 'forms'


