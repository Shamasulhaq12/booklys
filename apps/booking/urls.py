
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookingsViewSet,
    ServiceFeedbackViewSet,
    ClientFeedbackViewSet,
    JournalsViewSet,
    BookingDetailsForCalenderListing,
    BookingUsersList,
BookingDashboard
)

router = DefaultRouter()
router.register('bookings', BookingsViewSet, basename='bookings')
router.register('service-feedback', ServiceFeedbackViewSet, basename='service-feedback')
router.register('client-feedback', ClientFeedbackViewSet, basename='client-feedback')
router.register('journals', JournalsViewSet, basename='journals')

urlpatterns = [
    path('', include(router.urls)),
    path('booking-details-for-calender-listing/', BookingDetailsForCalenderListing.as_view(), name='booking-details-for-calender-listing'),
    path('booking-users-list/', BookingUsersList.as_view(), name='booking-users-list'),
    path('booking-dashboard/', BookingDashboard.as_view(), name='booking-dashboard'),
]
