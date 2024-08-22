from django_filters import rest_framework as backend_filters
from .models import Bookings

class BookingsFilter(backend_filters.FilterSet):
    name = backend_filters.CharFilter(field_name='name', lookup_expr='icontains')
    description = backend_filters.CharFilter(field_name='description', lookup_expr='icontains')
    max_price = backend_filters.NumberFilter(field_name='total_price', lookup_expr='lte')
    min_price = backend_filters.NumberFilter(field_name='total_price', lookup_expr='gte')

    class Meta:
        model = Bookings
        fields = ['name', 'description', 'price','booking_status', 'max_price', 'min_price']
