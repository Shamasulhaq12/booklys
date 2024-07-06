from rest_framework import serializers
from apps.payments_and_subscription.models import Subscription, SubscriptionFeature


class SubscriptionFeatureSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionFeature
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'feature_name': {'required': True},
        }


class SubscriptionSerializers(serializers.ModelSerializer):
    subscription_features = SubscriptionFeatureSerializers(many=True)

    class Meta:
        model = Subscription
        fields = '__all__'
        read_only_fields = ['id']
