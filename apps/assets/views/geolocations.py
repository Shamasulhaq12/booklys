from apps.assets.serializers import (
    CurrencySerializer, CitiesSerializer,
    CallingCodeWithNameSerializer, CountryTimeZoneSerializer,
    CountriesSerializer,
)
from rest_framework import viewsets


class CountriesViewSet(viewsets.ModelViewSet):
    serializer_class = CountriesSerializer
    queryset = CountriesSerializer.Meta.model.objects.all()


class CountryTimeZoneViewSet(viewsets.ModelViewSet):
    serializer_class = CountryTimeZoneSerializer
    queryset = CountryTimeZoneSerializer.Meta.model.objects.all()


class CallingCodeWithNameViewSet(viewsets.ModelViewSet):
    serializer_class = CallingCodeWithNameSerializer
    queryset = CallingCodeWithNameSerializer.Meta.model.objects.all()


class CitiesViewSet(viewsets.ModelViewSet):
    serializer_class = CitiesSerializer
    queryset = CitiesSerializer.Meta.model.objects.all()


class CurrencyViewSet(viewsets.ModelViewSet):
    serializer_class = CurrencySerializer
    queryset = CurrencySerializer.Meta.model.objects.all()
