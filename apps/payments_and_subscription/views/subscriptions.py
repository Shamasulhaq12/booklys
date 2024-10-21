from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.payments_and_subscription.serializers import SubscriptionSerializers, SubscriptionFeatureSerializers
from rest_framework.response import Response
from rest_framework import status


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializers
    queryset = SubscriptionSerializers.Meta.model.objects.filter(is_active=True)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]
        return super(self.__class__, self).get_permissions()

    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        subscription_features = serializers.validated_data.pop('subscription_features', [])
        subscription = serializers.save()
        for feature in subscription_features:
            feature_serializer = SubscriptionFeatureSerializers(data=feature)
            feature_serializer.is_valid(raise_exception=True)
            feature_serializer.save(subscription=subscription)
        return Response({
            'message': 'Subscription created successfully',
            'data': serializers.data
        }, status=status.HTTP_201_CREATED)