# Description: Filters for services app.
from django_filters import rest_framework as backend_filters
from .models import Services, Company


class ServicesFilter(backend_filters.FilterSet):
    min_price = backend_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = backend_filters.NumberFilter(field_name='price', lookup_expr='lte')
    min_duration = backend_filters.NumberFilter(field_name='duration', lookup_expr='gte')
    max_duration = backend_filters.NumberFilter(field_name='duration', lookup_expr='lte')
    start_date = backend_filters.DateFilter(field_name='start_date', method='start_date_filter')
    end_date = backend_filters.DateFilter(field_name='end_date', method='end_date_filter')

    class Meta:
        model = Services
        fields = [
            'category', 'company',
            'min_price', 'max_price', 'min_duration',
            'max_duration', 'service_type', 'company__address',
            'start_date', 'end_date'
            ]

    def start_date_filter(self, queryset, name, value):
        return queryset.exclude(service_bookings__start_booking_slot__gte=value)

    def end_date_filter(self, queryset, name, value):
        return queryset.exclude(service_bookings__end_booking_slot__lte=value)
