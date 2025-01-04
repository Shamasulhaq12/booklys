from apps.assets.models import Templates
from rest_framework import serializers


class TemplatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Templates
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')