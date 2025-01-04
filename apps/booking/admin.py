from django.contrib import admin
from .models import Bookings, ClientFeedback, ServiceFeedback, Journals, Diagnosis, KVACodes, JournalFiles

# Register your models here.

admin.site.register(Bookings)
admin.site.register(ClientFeedback)
admin.site.register(ServiceFeedback)
admin.site.register(Diagnosis)
admin.site.register(KVACodes)
@admin.register(JournalFiles)
class JournalFilesAdmin(admin.ModelAdmin):
    pass



@admin.register(Journals)
class JournalsAdmin(admin.ModelAdmin):
    pass