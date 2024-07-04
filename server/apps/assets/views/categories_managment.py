from apps.assets.serializers import CategoriesSerializer, SubCategoriesSerializer
from rest_framework import viewsets


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = CategoriesSerializer.Meta.model.objects.all()


class SubCategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = SubCategoriesSerializer
    queryset = SubCategoriesSerializer.Meta.model.objects.all()
