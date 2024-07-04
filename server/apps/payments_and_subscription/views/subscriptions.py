from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.payments_and_subscription.serializers import SubscriptionSerializers


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializers
    queryset = SubscriptionSerializers.Meta.model.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]
        return super(self.__class__, self).get_permissions()
