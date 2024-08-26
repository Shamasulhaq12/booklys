from .models import Company, CompanyImages, Services, CompanyStaff, BookingFields, StaffSlots
from rest_framework import serializers
from apps.booking.serializers import  ServiceFeedbackSerializer


class StaffSlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffSlots
        fields = '__all__'
        extra_kwargs = {
            'staff': {'required': False}
        }

class CompanyStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyStaff
        fields = '__all__'
        extra_kwargs = {
            'company': {'required': False}
        }


class BookingFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingFields
        fields = '__all__'
        extra_kwargs = {
            'service': {'required': False}
        }

class ServicesSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_id = serializers.IntegerField(source='category.id', read_only=True)
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
    company_staff = CompanyStaffSerializer(many=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_id = serializers.IntegerField(source='category.id', read_only=True)
    company_feedback = ServiceFeedbackSerializer(many=True, read_only=True)
    rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'
        extra_kwargs = {
            'owner': {'required': False}
        }
