from apps.assets.serializers import CategoriesSerializer, PriceGroupSerializer
from rest_framework import viewsets

from rest_framework import filters
from django_filters import rest_framework as backend_filters
from rest_framework.permissions import AllowAny
from utils.paginations.pagination import OurLimitOffsetPagination



class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = CategoriesSerializer.Meta.model.objects.all()
    pagination_class = OurLimitOffsetPagination

    permission_classes = [AllowAny]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        backend_filters.DjangoFilterBackend,
    ]
    ordering_fields = ['id', 'created_at', 'updated_at']

    search_fields = ['name', ]

class PriceGroupViewSet(viewsets.ModelViewSet):
    serializer_class = PriceGroupSerializer
    queryset = PriceGroupSerializer.Meta.model.objects.all()
    permission_classes = [AllowAny]