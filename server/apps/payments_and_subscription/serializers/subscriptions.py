from rest_framework import serializers
from apps.payments_and_subscription.models import Subscription


class SubscriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
        read_only_fields = ['id']
        