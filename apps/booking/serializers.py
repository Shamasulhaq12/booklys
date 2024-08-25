from rest_framework import serializers
from .models import Bookings, ClientFeedback, ServiceFeedback


class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'
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