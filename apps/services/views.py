from .serializers import CompanySerializer, CompanyStaffSerializer, ServicesSerializer, CompanyImagesSerializer
from rest_framework import viewsets
from rest_framework.generics import DestroyAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from .models import Company, CompanyImages, Services, CompanyStaff, BookingFields


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user.profile)

class PublicCompanyListAPIView(ListAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.exclude(is_active=True, owner=self.request.user.profile)
        return self.queryset.filter(is_active=True)

class PublicCompanyDetailAPIView(RetrieveAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.exclude(is_active=True, owner=self.request.user.profile)
        return self.queryset.filter(is_active=True)


class ServicesViewSet(viewsets.ModelViewSet):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()

    def get_queryset(self):
        return self.queryset.filter(company__owner=self.request.user.profile)

    def perform_create(self, serializer):
        booking_fields = serializer.validated_data.pop('service_booking_fields', None)
        service = serializer.save()
        if booking_fields:
            for field in booking_fields:
                BookingFields.objects.create(service=service, **field)

class PublicServicesListAPIView(ListAPIView):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.exclude(company__owner=self.request.user.profile)
        return self.queryset.filter(company__is_active=True)

class PublicServicesDetailAPIView(RetrieveAPIView):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.exclude(company__owner=self.request.user.profile)
        return self.queryset.filter(company__is_active=True)



class RemoveCompanyStaffAPIView(DestroyAPIView):
    queryset = CompanyStaff.objects.all()
    serializer_class = CompanyStaffSerializer

    def get_queryset(self):
        return self.queryset.filter(company__owner=self.request.user.profile)


class RemoveServicesAPIView(DestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

    def get_queryset(self):
        return self.queryset.filter(company__owner=self.request.user.profile)


class RemoveCompanyImagesAPIView(DestroyAPIView):
    queryset = CompanyImages.objects.all()
    serializer_class = CompanyImagesSerializer

    def get_queryset(self):
        return self.queryset.filter(company__owner=self.request.user.profile)


class UpdateCompanyStaffAPIView(UpdateAPIView):
    queryset = CompanyStaff.objects.all()
    serializer_class = CompanyStaffSerializer

    def get_queryset(self):
        return self.queryset.filter(company__owner=self.request.user.profile)


class UpdateCompanyServicesAPIView(UpdateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

    def get_queryset(self):
        return self.queryset.filter(company__owner=self.request.user.profile)


class UpdateCompanyImagesAPIView(UpdateAPIView):
    queryset = CompanyImages.objects.all()
    serializer_class = CompanyImagesSerializer

    def get_queryset(self):
        return self.queryset.filter(company__owner=self.request.user.profile)

