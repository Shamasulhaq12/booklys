from apps.core.models import LogEntry
from rest_framework import serializers


class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
