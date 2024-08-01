from rest_framework_simplejwt.views import TokenObtainPairView
from apps.core.serializers import UserDetailSerializer
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user= get_object_or_404(User, email=request.data['email'])
        serializer = UserDetailSerializer(user)
        return Response({
            'access': response.data['access'],
            'refresh': response.data['refresh'],
            'user': serializer.data,
            'is_payment_verified': user.profile.is_payment_verified
        }, status=status.HTTP_200_OK)




















