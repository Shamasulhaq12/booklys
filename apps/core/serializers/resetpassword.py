from rest_framework import serializers


class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField()
