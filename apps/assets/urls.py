
from django.urls import path, include
from apps.assets.views import (
    CountriesViewSet, CountryTimeZoneViewSet,
    CallingCodeWithNameViewSet, CitiesViewSet,
    CurrencyViewSet, CategoriesViewSet,
)

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'countries', CountriesViewSet, 'countries')
router.register(r'country-timezone', CountryTimeZoneViewSet, 'country-timezone')
router.register(r'calling-code', CallingCodeWithNameViewSet, 'calling-code')
router.register(r'cities', CitiesViewSet, 'cities')
router.register(r'currency', CurrencyViewSet, 'currency')
router.register(r'categories', CategoriesViewSet, 'categories')

urlpatterns = [
    path('', include(router.urls)),

]
