from rest_framework import serializers
from .models import Bookings, ClientFeedback, ServiceFeedback


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
    class Meta:
        model = Bookings
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


