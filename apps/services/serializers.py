from .models import Company, CompanyImages, Services, CompanyStaff, ServicePrice, BookingFields
from rest_framework import serializers


class CompanyStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyStaff
        fields = '__all__'


class BookingFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingFields
        fields = '__all__'

class ServicePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePrice
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_id = serializers.IntegerField(source='category.id', read_only=True)
    service_price = ServicePriceSerializer(many=True)
    service_booking_fields = BookingFieldsSerializer(many=True)
    class Meta:
        model = Services
        fields = '__all__'


class CompanyImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyImages
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    company_images = CompanyImagesSerializer(many=True, read_only=True)
    company_services = ServicesSerializer(many=True, read_only=True)
    company_staff = CompanyStaffSerializer(many=True, read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_id = serializers.IntegerField(source='category.id', read_only=True)

    class Meta:
        model = Company
        fields = '__all__'
