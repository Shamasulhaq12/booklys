from rest_framework import serializers
from .models import Bookings, ClientFeedback, ServiceFeedback, Journals
from apps.userprofile.models import UserProfile
import datetime
from .helper import is_slot_available


class BookingUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'user', 'image',]
        read_only_fields = ('created_at', 'updated_at')


class ClientFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientFeedback
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class ServiceFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceFeedback
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class BookingsSerializer(serializers.ModelSerializer):
    booking_feedback = ClientFeedbackSerializer(many=True, read_only=True)
    company_name = serializers.CharField(source='service.company.name', read_only=True)
    service_name = serializers.CharField(source='service.service_name', read_only=True)
    service_timing = serializers.CharField(source='service.service_timing', read_only=True)
    company_image = serializers.SerializerMethodField()


    class Meta:
        model = Bookings
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
    def get_company_image(self, obj):
        try:
            return obj.service.company.company_images.first().image.url
        except:
            return None



    def validate(self, attrs):
        if attrs['booking_date'] < datetime.date.today():
            raise serializers.ValidationError('Booking date cannot be in the past')
        if attrs['start_booking_slot'] >= attrs['end_booking_slot']:
            raise serializers.ValidationError('Start time must be before end time')
        if is_slot_available(attrs['service'], attrs['booking_date'], attrs['start_booking_slot'], attrs['end_booking_slot']):
            raise serializers.ValidationError('Slot is not available')
        return attrs


class JournalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journals
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')