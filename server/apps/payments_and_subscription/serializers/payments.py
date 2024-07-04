from rest_framework import serializers
from apps.payments_and_subscription.models import PaymentDetails, PayPalUserDetail


class PaymentDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = '__all__'
        read_only_fields = ['id']


class PaypalUserDetailsSerializer(serializers.ModelSerializer):
    """Serializer for user paypal payment details."""
    class Meta:
        model = PayPalUserDetail
        fields = ('paypal_email', 'user', 'id', 'created_at', 'updated_at',)
        read_only_fields = ('user', 'id',)
