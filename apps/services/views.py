from .serializers import CompanySerializer, CompanyStaffSerializer, ServicesSerializer, CompanyImagesSerializer

from rest_framework import viewsets
from rest_framework.generics import DestroyAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from .models import Company, CompanyImages, Services, CompanyStaff, BookingFields, StaffSlots
from django.db.models import Avg


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.annotate(rating=Avg('company_feedback__rating'))


    def perform_create(self, serializer):
        owner = self.request.user.profile
        company_staff = serializer.validated_data.pop('company_staff', None)
        if company_staff:
            company = serializer.save(owner=owner)
            for staff in company_staff:
                slots = staff.pop('staff_slots', None)
                staff = CompanyStaff.objects.create(company=company, **staff)
                if slots:
                    for slot in slots:
                        StaffSlots.objects.create(staff=staff, **slot)
        else:
            serializer.save(owner=owner)

    def perform_update(self, serializer):
        company_staff = serializer.validated_data.pop('company_staff', None)
        company = serializer.save()
        if company_staff:
            company.company_staff.all().delete()
            for staff in company_staff:
                slots = staff.pop('staff_slots', None)
                staff = CompanyStaff.objects.create(company=company, **staff)
                if slots:
                    for slot in slots:
                        StaffSlots.objects.create(staff=staff, **slot)
        else:
            serializer.save()
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

