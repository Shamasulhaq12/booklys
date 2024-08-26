# Description: Filters for services app.
from django_filters import rest_framework as backend_filters
from .models import Services, Company


class ServicesFilter(backend_filters.FilterSet):
    min_price = backend_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = backend_filters.NumberFilter(field_name='price', lookup_expr='lte')
    min_duration = backend_filters.NumberFilter(field_name='duration', lookup_expr='gte')
    max_duration = backend_filters.NumberFilter(field_name='duration', lookup_expr='lte')

    class Meta:
        model = Services
        fields = ['category', 'company', 'min_price', 'max_price', 'min_duration', 'max_duration','service_type']