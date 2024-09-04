from rest_framework import viewsets
from .serializers import BookingsSerializer, ClientFeedbackSerializer, ServiceFeedbackSerializer, JournalsSerializer
from rest_framework import filters
from django_filters import rest_framework as backend_filters
from .filters import BookingsFilter
from utils.paginations import OurLimitOffsetPagination



class JournalsViewSet(viewsets.ModelViewSet):
    serializer_class = JournalsSerializer
    queryset = JournalsSerializer.Meta.model.objects.all()
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        backend_filters.DjangoFilterBackend,
    ]
    search_fields = ['name', 'description']
    ordering_fields = ['id', 'created_at', 'updated_at']
    filterset_fields = ['name', 'description']
    pagination_class = OurLimitOffsetPagination
    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user.profile)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)



class ClientFeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = ClientFeedbackSerializer
    queryset = ClientFeedbackSerializer.Meta.model.objects.all()
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        backend_filters.DjangoFilterBackend,
    ]
    ordering_fields = ['id', 'created_at', 'updated_at']
    filterset_fields = ['rating', 'feedback']
    pagination_class = OurLimitOffsetPagination

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.user_type == 'supplier':
                return self.queryset.filter(service__supplier=self.request.user.profile)
            return self.queryset.filter(user=self.request.user.profile)
        return self.queryset.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user.profile)

class ServiceFeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceFeedbackSerializer
    queryset = ServiceFeedbackSerializer.Meta.model.objects.all()
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        backend_filters.DjangoFilterBackend,
    ]
    ordering_fields = ['id', 'created_at', 'updated_at']
    filterset_fields = ['rating', 'feedback']
    pagination_class = OurLimitOffsetPagination

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.user_type == 'supplier':
                return self.queryset.filter(service__supplier=self.request.user.profile)
            return self.queryset.filter(user=self.request.user.profile)
        return self.queryset.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user.profile)


class BookingsViewSet(viewsets.ModelViewSet):
    serializer_class = BookingsSerializer
    queryset = BookingsSerializer.Meta.model.objects.all()
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        backend_filters.DjangoFilterBackend,
    ]
    search_fields = ['name', 'description', 'total_price']
    ordering_fields = ['id', 'total_price', 'created_at', 'updated_at']
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



