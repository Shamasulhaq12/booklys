from apps.assets.models import Countries, CountryTimeZone, CallingCodeWithName, Cities, Currency
from rest_framework import serializers


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = '__all__'


class CountryTimeZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryTimeZone
        fields = '__all__'


class CallingCodeWithNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallingCodeWithName
        fields = '__all__'


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'
