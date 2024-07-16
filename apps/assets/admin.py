from django.contrib import admin
from apps.assets.models import (
    Countries, CountryTimeZone, CallingCodeWithName, Cities, Currency, Categories,
)


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ('common_name', 'official_name', 'alpha_code_2', 'alpha_code_3')
    list_filter = ('common_name', 'official_name', 'alpha_code_2', 'alpha_code_3')
    search_fields = ('common_name', 'official_name', 'alpha_code_2', 'alpha_code_3')


@admin.register(CountryTimeZone)
class CountryTimeZoneAdmin(admin.ModelAdmin):
    list_display = ('country', 'timezone')
    list_filter = ('country', 'timezone')
    search_fields = ('country', 'timezone')


@admin.register(CallingCodeWithName)
class CallingCodeWithNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'calling_code')
    list_filter = ('name', 'calling_code')
    search_fields = ('name', 'calling_code')


@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('country', 'name')
    list_filter = ('country', 'name')
    search_fields = ('country', 'name')


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    list_filter = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )

