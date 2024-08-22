from rest_framework import viewsets
from .serializers import BookingsSerializer
from rest_framework import filters
from django_filters import rest_framework as backend_filters
from .filters import BookingsFilter
from utils.paginations import OurLimitOffsetPagination




class BookingsViewSet(viewsets.ModelViewSet):
    serializer_class = BookingsSerializer
    queryset = BookingsSerializer.Meta.model.objects.all()
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        backend_filters.DjangoFilterBackend,
    ]
    search_fields = ['name', 'description', 'price']
    ordering_fields = ['id', 'price', 'created_at', 'updated_at']
    filterset_class = BookingsFilter
    pagination_class = OurLimitOffsetPagination

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.user_type == 'supplier':
                return self.queryset.filter(service__supplier=self.request.user.profile)
            return self.queryset.filter(user=self.request.user.profile)
        return self.queryset.none()

    def perform_create(self, serializer):
        instance = serializer.instance
        additional_services = instance.service.additional_services.all()
        total_price= instance.service.price
        if additional_services.exists():
            for service in additional_services:
                if service.is_free:
                    total_price += service.price
        serializer.save(total_price=total_price)

    def perform_update(self, serializer):
        instance = serializer.instance
        additional_services = instance.service.additional_services.all()
        total_price= instance.service.price
        if additional_services.exists():
            for service in additional_services:
                if service.is_free:
                    total_price += service.price
        serializer.save(total_price=total_price)



