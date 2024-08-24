from apps.assets.serializers import (
    CurrencySerializer, CitiesSerializer,
    CallingCodeWithNameSerializer, CountryTimeZoneSerializer,
    CountriesSerializer,
)
from rest_framework.permissions import AllowAny
from rest_framework import viewsets


class CountriesViewSet(viewsets.ModelViewSet):
    serializer_class = CountriesSerializer
    permission_classes = [AllowAny]
    queryset = CountriesSerializer.Meta.model.objects.all()


class CountryTimeZoneViewSet(viewsets.ModelViewSet):
    serializer_class = CountryTimeZoneSerializer
    permission_classes = [AllowAny]
    queryset = CountryTimeZoneSerializer.Meta.model.objects.all()


class CallingCodeWithNameViewSet(viewsets.ModelViewSet):
    serializer_class = CallingCodeWithNameSerializer
    permission_classes = [AllowAny]
    queryset = CallingCodeWithNameSerializer.Meta.model.objects.all()


class CitiesViewSet(viewsets.ModelViewSet):
    serializer_class = CitiesSerializer
    permission_classes = [AllowAny]
    queryset = CitiesSerializer.Meta.model.objects.all()


class CurrencyViewSet(viewsets.ModelViewSet):
    serializer_class = CurrencySerializer
    permission_classes = [AllowAny]
    queryset = CurrencySerializer.Meta.model.objects.all()
