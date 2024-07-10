from .models import Company, CompanyImages, CompanyServices, CompanyStaff
from rest_framework import serializers


class CompanyStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyStaff
        fields = '__all__'


class CompanyServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyServices
        fields = '__all__'


class CompanyImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyImages
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    company_images = CompanyImagesSerializer(many=True, read_only=True)
    company_services = CompanyServicesSerializer(many=True, read_only=True)
    company_staff = CompanyStaffSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = '__all__'
