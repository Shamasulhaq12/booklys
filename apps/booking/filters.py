from django_filters import rest_framework as backend_filters
from .models import Bookings

class BookingsFilter(backend_filters.FilterSet):

    name = backend_filters.CharFilter(field_name='name', lookup_expr='icontains')
    description = backend_filters.CharFilter(field_name='description', lookup_expr='icontains')
    max_price = backend_filters.NumberFilter(field_name='total_price', lookup_expr='lte')
    min_price = backend_filters.NumberFilter(field_name='total_price', lookup_expr='gte')
    previous_date_booking = backend_filters.DateFilter(field_name='booking_date', lookup_expr='lt')
    upcoming_date_booking = backend_filters.DateFilter(field_name='booking_date', lookup_expr='gt')

    class Meta:
        model = Bookings
        fields = ['name', 'description','booking_status', 'max_price', 'min_price', 'previous_date_booking', 'upcoming_date_booking']
