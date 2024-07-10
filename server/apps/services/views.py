from .serializers import CompanySerializer, CompanyStaffSerializer, CompanyServicesSerializer, CompanyImagesSerializer
from rest_framework import viewsets
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from .models import Company, CompanyImages, CompanyServices, CompanyStaff


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user.profile)

    def perform_create(self, serializer):
        company_images = serializer.validated_data.pop('company_images', None)
        company_services = serializer.validated_data.pop('company_services', None)
        company_staff = serializer.validated_data.pop('company_staff', None)
        company = serializer.save(owner=self.request.user.profile)
        for image in company_images:
            CompanyImages.objects.create(company=company, **image)
        for service in company_services:
            CompanyServices.objects.create(company=company, **service)
        for staff in company_staff:
            CompanyStaff.objects.create(company=company, **staff)

    def perform_update(self, serializer):
        company_images = serializer.validated_data.pop('company_images', None)
        company_services = serializer.validated_data.pop('company_services', None)
        company_staff = serializer.validated_data.pop('company_staff', None)
        company = serializer.save(owner=self.request.user.profile)
        for image in company_images:
            CompanyImages.objects.create(company=company, **image)
        for service in company_services:
            CompanyServices.objects.create(company=company, **service)
        for staff in company_staff:
            CompanyStaff.objects.create(company=company, **staff)



class RemoveCompanyStaffAPIView(DestroyAPIView):
    queryset = CompanyStaff.objects.all()
    serializer_class = CompanyStaffSerializer

    def get_queryset(self):
        return self.queryset.filter(company__owner=self.request.user.profile)


class RemoveCompanyServicesAPIView(DestroyAPIView):
    queryset = CompanyServices.objects.all()
    serializer_class = CompanyServicesSerializer

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
    queryset = CompanyServices.objects.all()
    serializer_class = CompanyServicesSerializer

    def get_queryset(self):
        return self.queryset.filter(company__owner=self.request.user.profile)


class UpdateCompanyImagesAPIView(UpdateAPIView):
    queryset = CompanyImages.objects.all()
    serializer_class = CompanyImagesSerializer

    def get_queryset(self):
        return self.queryset.filter(company__owner=self.request.user.profile)

