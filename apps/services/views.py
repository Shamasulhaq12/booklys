from .serializers import CompanySerializer, CompanyStaffSerializer, ServicesSerializer, CompanyImagesSerializer

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from .models import Company, CompanyImages, Services, CompanyStaff, BookingFields, StaffSlots
from django.db.models import Avg
from .filters import ServicesFilter
from rest_framework import filters
from django_filters import rest_framework as backend_filters
from rest_framework.response import Response
from .serializers import StaffSlotsSerializer


class AvailableStaffSlotsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        service = self.request.GET.get('service')
        staff = self.request.GET.get('staff')
        slots = StaffSlots.objects.filter(staff=staff)
        filtered_slots = []
        for slot in slots:
            if slot.is_active and slot.start_time >= service.start_time and slot.end_time <= service.end_time:
                filtered_slots.append(slot)
        serializer = StaffSlotsSerializer(filtered_slots, many=True)
        return Response(serializer.data)



class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.annotate(rating=Avg('company_feedback__rating'))
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        backend_filters.DjangoFilterBackend,
    ]
    ordering_fields = ['id', 'created_at', 'updated_at']
    filterset_fields = ['category', 'is_active']
    search_fields = ['name', 'company_description']


    def perform_create(self, serializer):
        owner = self.request.user.profile
        company_staff = serializer.validated_data.pop('company_staff', None)
        if company_staff:
            company = serializer.save(owner=owner)
            for staff in company_staff:
                staff = CompanyStaff.objects.create(company=company, **staff)
        else:
            serializer.save(owner=owner)

    def perform_update(self, serializer):
        company_staff = serializer.validated_data.pop('company_staff', None)
        company = serializer.save()
        if company_staff:
            company.company_staff.all().delete()
            for staff in company_staff:
                staff = CompanyStaff.objects.create(company=company, **staff)
        else:
            serializer.save()
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user.profile)


class PublicCompanyListAPIView(ListAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        backend_filters.DjangoFilterBackend,
    ]
    ordering_fields = ['id', 'created_at', 'updated_at']
    filterset_fields = ['category', 'is_active']
    search_fields = ['name', 'company_description']

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
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        backend_filters.DjangoFilterBackend,
    ]
    ordering_fields = ['id', 'created_at', 'updated_at']
    filterset_class = ServicesFilter
    search_fields = ['service_name', 'service_description']

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
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        backend_filters.DjangoFilterBackend,
    ]
    ordering_fields = ['id', 'created_at', 'updated_at']
    filterset_class = ServicesFilter
    search_fields = ['service_name', 'service_description']


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

