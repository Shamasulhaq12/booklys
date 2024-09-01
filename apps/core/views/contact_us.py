from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from apps.core.models import ContactUs
from ..serializers.contact_us import ContactUsSerializer


class ContactUsCreateAPIView(CreateAPIView):
    """ This class is used to create the contact us """
    serializer_class = ContactUsSerializer

    def post(self, request, *args, **kwargs):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

