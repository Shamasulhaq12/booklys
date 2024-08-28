from .models import Company, CompanyImages, Services, CompanyStaff, BookingFields, ContactInformation, WorkSchedule
from rest_framework import serializers
from apps.booking.serializers import  ServiceFeedbackSerializer


class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = '__all__'
        extra_kwargs = {
            'staff': {'required': False}
        }

class WorkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSchedule
        fields = '__all__'
        extra_kwargs = {
            'staff': {'required': False}
        }


class CompanyStaffSerializer(serializers.ModelSerializer):

    staff_contacts = ContactInformationSerializer(many=True, required=False)
    work_schedule = WorkScheduleSerializer(many=True, required=False)
    calling_code = serializers.CharField(source='calling_code.calling_code', read_only=True)

    class Meta:
        model = CompanyStaff
        fields = '__all__'
        extra_kwargs = {
            'company': {'required': False}
        }

    def get_staff_rating(self, obj):
        return 1

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
    service_provider_first_name = serializers.CharField(source='service_provider.first_name', read_only=True)
    service_provider_last_name = serializers.CharField(source='service_provider.last_name', read_only=True)
    service_provider_email = serializers.CharField(source='service_provider.email', read_only=True)
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
