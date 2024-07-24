from apps.assets.models import Categories, PriceGroup
from rest_framework import serializers


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class PriceGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceGroup
        fields = '__all__'
