from django.db import models
from coresite.mixin import AbstractTimeStampModel

class LogEntry(AbstractTimeStampModel):
    ip_address = models.GenericIPAddressField()
    activity = models.TextField()
    user = models.CharField(max_length=255, null=True, blank=True)
    person = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.created_at} - {self.activity}"
