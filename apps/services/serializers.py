from .models import Company, CompanyImages, Services, CompanyStaff, BookingFields, ContactInformation, WorkSchedule, Slots
from rest_framework import serializers
from apps.booking.serializers import  ServiceFeedbackSerializer


class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = '__all__'
        extra_kwargs = {
            'staff': {'required': False}
        }


class SlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slots
        fields = '__all__'
        extra_kwargs = {
            'work_schedule': {'required': False}
        }


class WorkScheduleSerializer(serializers.ModelSerializer):
    staff_slots = SlotsSerializer(many=True, required=False)
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
    company_name = serializers.CharField(source='company.name', read_only=True)
    company_id = serializers.IntegerField(source='company.id', read_only=True)

    class Meta:
        model = CompanyStaff
        fields = '__all__'
        extra_kwargs = {
            'company': {'required': False}
        }

    def get_staff_rating(self, obj):
        return 1

class UpdateCompanyStaffImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyStaff
        fields = ['image']


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
    service_providers = CompanyStaffSerializer(many=True, read_only=True)
    class Meta:
        model = Services
        fields = '__all__'


class CompanyImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyImages
        fields = '__all__'
        extra_kwargs = {
            'company': {'required': False}
        }


class CompanySerializer(serializers.ModelSerializer):
    company_images = CompanyImagesSerializer(many=True)
    company_services = ServicesSerializer(many=True, read_only=True)
    company_staff = CompanyStaffSerializer(many=True,read_only=True)
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
