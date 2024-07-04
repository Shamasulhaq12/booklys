from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from apps.payments_and_subscription.serializers import PaypalUserDetailsSerializer


class CreatePaypalUserDetailsView(CreateAPIView):
    serializer_class = PaypalUserDetailsSerializer
    permission_classes = [IsAuthenticated]
    queryset = PaypalUserDetailsSerializer.Meta.model.objects.all()

    def create(self, request, *args, **kwargs):
        if PaypalUserDetailsSerializer.Meta.model.objects.filter(user=request.user.profile).exists():
            return Response({
                'message': 'Paypal user details already exists'
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializers = self.get_serializer(data=request.data)
            serializers.is_valid(raise_exception=True)
            serializers.save(user=request.user.profile)
            return Response({
                'message': 'Paypal user details created successfully',
                'data': serializers.data
            }, status=status.HTTP_201_CREATED)


class PaypalUserDetailsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PaypalUserDetailsSerializer
    permission_classes = [IsAuthenticated]
    queryset = PaypalUserDetailsSerializer.Meta.model.objects.all()

    def get_object(self):
        print(self.request.user.profile.paypal_user_details)
        return self.request.user.profile.paypal_user_details
