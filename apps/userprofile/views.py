from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import UserProfile
from rest_framework import filters
from utils.paginations.pagination import LimitOffsetPagination
from django_filters import rest_framework as backend_filters
from .filters import UserProfileFilter
from .serializers import UserProfileSerializer, PatientFilesSerializer


class PatientFilesViewSet(viewsets.ModelViewSet):
    queryset = PatientFilesSerializer.Meta.model.objects.all()
    serializer_class = PatientFilesSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = IsAdminUser
    filter_backends = [
        backend_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ['user','file_type']
# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    pagination_class = LimitOffsetPagination
    filter_backends = [
        backend_filters.DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_class = UserProfileFilter
    search_fields = ['first_name', 'last_name', 'user__username']
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'user__username'
    lookup_url_kwarg = 'username'

    def get_queryset(self):
        if self.action == 'list' or self.action == 'retrieve':
            return self.queryset.filter(user__is_active=True)
        return self.queryset.filter(user__is_active=True, user=self.request.user)

    def perform_update(self, serializer):
        serializer.save()

    def perform_create(self, serializer):
        serializer.save()
