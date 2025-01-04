
from django.urls import path, include
from django.urls import re_path
from .views import UserProfileViewSet, PatientFilesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user-profile', UserProfileViewSet, basename='userprofile')
router.register('patient-files', PatientFilesViewSet, basename='patient-files')

urlpatterns = [
    path('', include(router.urls)),

]
