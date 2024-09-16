from .serializers import CompanySerializer, CompanyStaffSerializer, ServicesSerializer, CompanyImagesSerializer,UpdateCompanyStaffImageSerializer, WorkScheduleSerializer

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from .models import (Company, CompanyImages, Services, CompanyStaff,
                     BookingFields, ContactInformation, WorkSchedule, Slots)
from django.db.models import Avg
from .filters import ServicesFilter
from rest_framework import filters
from django_filters import rest_framework as backend_filters
from rest_framework.response import Response
from rest_framework import status
from .helper import create_time_slots

class AvailableStaffSlotsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        staff = self.request.GET.get('staff')

        if staff:
            company_staff = WorkSchedule.objects.filter(staff=staff)
            serialized_data = WorkScheduleSerializer(company_staff, many=True)

            return Response(serialized_data.data, status=status.HTTP_200_OK)
        return Response({'error': 'Staff id is required'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateCompanyStaffImageAPIView(UpdateAPIView):
    queryset = CompanyStaff.objects.all()
    serializer_class = UpdateCompanyStaffImageSerializer

    def get_queryset(self):
        return self.queryset.filter(company__owner=self.request.user.profile)


class CompanyStaffViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyStaffSerializer
    queryset = CompanyStaff.objects.all()
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        backend_filters.DjangoFilterBackend,
    ]
    ordering_fields = ['id', 'created_at', 'updated_at']
    filterset_fields = ['is_active']
    search_fields = ['first_name', 'last_name', 'email']

    def get_queryset(self):
        return self.queryset.filter(company__owner=self.request.user.profile)

    def perform_create(self, serializer):
        staff_contacts = serializer.validated_data.pop('staff_contacts', None)
        work_schedule = serializer.validated_data.pop('work_schedule', None)
        staff = serializer.save()

        if staff_contacts:
            for contact in staff_contacts:
                ContactInformation.objects.create(staff=staff, **contact)
        if work_schedule:
            for schedule in work_schedule:
                work_schedule=WorkSchedule.objects.create(staff=staff, **schedule)

                slots = create_time_slots(work_schedule.start_time, work_schedule.end_time,
                                          work_schedule.start_break_time, work_schedule.end_break_time)
                for slot in slots:
                    Slots.objects.create(work_schedule=work_schedule, **slot)

    def perform_update(self, serializer):
        staff_contacts = serializer.validated_data.pop('staff_contacts', None)
        work_schedule = serializer.validated_data.pop('work_schedule', None)
        serializer.save()
        staff= serializer.instance
        if staff_contacts:
            staff.staff_contacts.all().delete()
            for contact in staff_contacts:
                ContactInformation.objects.create(staff=staff, **contact)
        if work_schedule:
            staff.work_schedule.all().delete()
            for schedule in work_schedule:
                work_schedule=WorkSchedule.objects.create(staff=staff, **schedule)
                slots = create_time_slots(work_schedule.start_time, work_schedule.end_time,
                                          work_schedule.start_break_time, work_schedule.end_break_time)
                for slot in slots:
                    Slots.objects.create(work_schedule=work_schedule, **slot)


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.annotate(rating=Avg('company_feedback__rating'))
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        backend_filters.DjangoFilterBackend,
    ]
    ordering_fields = ['id', 'created_at', 'updated_at']
    filterset_fields = [ 'is_active']
    search_fields = ['name', 'company_description', 'company_services__service_name']


    def perform_create(self, serializer):
        owner = self.request.user.profile
        company_staff = serializer.validated_data.pop('company_staff', None)
        company_images = serializer.validated_data.pop('company_images', None)
        if company_images:
            company = serializer.save(owner=owner)
            for image in company_images:
                CompanyImages.objects.create(company=company, **image)
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
    filterset_fields = [ 'company_services__category__id','is_active']
    search_fields = ['name', 'company_description', 'company_services__service_name']

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

    def create(self, request, *args, **kwargs):
        service_providers = self.request.data.pop('service_providers', None)
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        booking_fields = serializer.validated_data.pop('service_booking_fields', None)

        service = serializer.save()
        if service_providers:
            for provider in service_providers:
                service.service_providers.add(provider)
        if booking_fields:
            for field in booking_fields:
                BookingFields.objects.create(service=service, **field)
        return Response(serializer.data, status=201)
    def update(self, request, *args, **kwargs):
        service_providers = self.request.data.pop('service_providers', None)
        booking_fields = self.request.data.pop('service_booking_fields', None)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        service = serializer.save()
        if service_providers:
            service.service_providers.clear()
            for provider in service_providers:
                service.service_providers.add(provider)
        if booking_fields:
            service.service_booking_fields.all().delete()
            for field in booking_fields:
                BookingFields.objects.create(service=service, **field)
        return Response(serializer.data, status=200)


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

