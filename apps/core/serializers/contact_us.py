from rest_framework import serializers
from apps.core.models import ContactUs

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']