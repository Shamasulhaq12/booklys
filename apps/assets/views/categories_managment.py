from apps.assets.serializers import CategoriesSerializer, PriceGroupSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = CategoriesSerializer.Meta.model.objects.all()
    permission_classes = [AllowAny]

class PriceGroupViewSet(viewsets.ModelViewSet):
    serializer_class = PriceGroupSerializer
    queryset = PriceGroupSerializer.Meta.model.objects.all()
    permission_classes = [AllowAny]