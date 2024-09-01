from django.db import models

from coresite.mixin import AbstractTimeStampModel


class ContactUs(AbstractTimeStampModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'
        db_table = 'contact_us'
        ordering = ['-id']
        indexes = [
            models.Index(fields=['-id']),
            models.Index(fields=['-created_at']),
        ]