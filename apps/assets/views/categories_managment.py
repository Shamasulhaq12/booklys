from apps.assets.serializers import CategoriesSerializer
from rest_framework import viewsets


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = CategoriesSerializer.Meta.model.objects.all()


