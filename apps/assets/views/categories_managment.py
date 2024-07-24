from apps.assets.serializers import CategoriesSerializer, PriceGroupSerializer
from rest_framework import viewsets


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = CategoriesSerializer.Meta.model.objects.all()

class PriceGroupViewSet(viewsets.ModelViewSet):
    serializer_class = PriceGroupSerializer
    queryset = PriceGroupSerializer.Meta.model.objects.all()