
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookingsViewSet,
    ServiceFeedbackViewSet,
    ClientFeedbackViewSet
)

router = DefaultRouter()
router.register('bookings', BookingsViewSet, basename='bookings')
router.register('service-feedback', ServiceFeedbackViewSet, basename='service-feedback')
router.register('client-feedback', ClientFeedbackViewSet, basename='client-feedback')

urlpatterns = [
    path('', include(router.urls)),

]
