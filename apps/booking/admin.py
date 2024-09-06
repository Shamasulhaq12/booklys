from django.contrib import admin
from .models import Bookings, ClientFeedback, ServiceFeedback, Journals

# Register your models here.

admin.site.register(Bookings)
admin.site.register(ClientFeedback)
admin.site.register(ServiceFeedback)
@admin.register(Journals)
class JournalsAdmin(admin.ModelAdmin):
    pass