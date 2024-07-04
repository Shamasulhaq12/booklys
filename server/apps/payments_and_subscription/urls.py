
from django.urls import path, include
from .views import SubscriptionViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('subscriptions', SubscriptionViewSet, basename='subscription')
urlpatterns = [
    path('', include(router.urls)),

]
