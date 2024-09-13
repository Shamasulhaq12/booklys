from django.contrib import admin
from .models import Company, CompanyImages, Services, CompanyStaff, WorkSchedule, ContactInformation


class CompanyImagesInline(admin.TabularInline):
    model = CompanyImages
    extra = 1


class CompanyServicesInline(admin.TabularInline):
    model = Services
    extra = 1


class CompanyStaffInline(admin.TabularInline):
    model = CompanyStaff
    extra = 1


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [CompanyImagesInline, CompanyServicesInline, CompanyStaffInline]
    list_display = ['name', 'owner', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'owner__username']

@admin.register(WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = [ 'day', 'start_time', 'end_time']
    list_filter = ['day']
    search_fields = [ 'day']
