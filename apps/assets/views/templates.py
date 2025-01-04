from apps.assets.serializers import TemplatesSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class TemplatesViewSet(viewsets.ModelViewSet):
    queryset = TemplatesSerializer.Meta.model.objects.all()
    serializer_class = TemplatesSerializer
    permission_classes = [IsAuthenticated]