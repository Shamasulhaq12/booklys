from rest_framework import serializers
from .models import Bookings, ClientFeedback, ServiceFeedback
import datetime
from .helper import is_slot_available



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
    available_slots = serializers.SerializerMethodField()
    class Meta:
        model = Bookings
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')



    def validate(self, attrs):
        if attrs['booking_date'] < datetime.date.today():
            raise serializers.ValidationError('Booking date cannot be in the past')
        if attrs['start_time'] >= attrs['end_time']:
            raise serializers.ValidationError('Start time must be before end time')
        if is_slot_available(attrs['service'], attrs['booking_date'], attrs['start_time'], attrs['end_time']):
            raise serializers.ValidationError('Slot is not available')
        return attrs
