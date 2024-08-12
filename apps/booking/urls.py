
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookingsViewSet
)

router = DefaultRouter()
router.register('bookings', BookingsViewSet, basename='bookings')

urlpatterns = [
    path('', include(router.urls)),

]
