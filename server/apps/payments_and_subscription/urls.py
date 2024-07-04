
from django.urls import path, include
from .views import SubscriptionViewSet, PaypalUserDetailsRetrieveUpdateDestroyView, CreatePaypalUserDetailsView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('subscriptions', SubscriptionViewSet, basename='subscription')
urlpatterns = [
    path('', include(router.urls)),
    path('create-paypal-user-details/', CreatePaypalUserDetailsView.as_view(), name='paypal-user-details'),
    path('urd_paypal-user-details/', PaypalUserDetailsRetrieveUpdateDestroyView.as_view(),
         name='paypal-user-details'),


]
