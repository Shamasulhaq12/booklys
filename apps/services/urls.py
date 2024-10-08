
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CompanyViewSet, RemoveServicesAPIView,
    RemoveCompanyImagesAPIView, RemoveCompanyStaffAPIView,
    UpdateCompanyServicesAPIView, UpdateCompanyImagesAPIView, UpdateCompanyStaffAPIView,
    ServicesViewSet, PublicServicesListAPIView, PublicServicesDetailAPIView,
    PublicCompanyListAPIView, PublicCompanyDetailAPIView,
CompanyStaffViewSet,
AvailableStaffSlotsAPIView,
UpdateCompanyStaffImageAPIView,
)


router = DefaultRouter()
router.register('company', CompanyViewSet, basename='company')
router.register('services', ServicesViewSet, basename='services')
router.register('company-staff', CompanyStaffViewSet, basename='company-staff')


urlpatterns = [
    path('', include(router.urls)),
    path('available-staff-slots/', AvailableStaffSlotsAPIView.as_view(), name='available-staff-slots'),
    path('update-company-staff-image/<int:pk>/', UpdateCompanyStaffImageAPIView.as_view(), name='update-company-staff-image'),
    path('public-services/', PublicServicesListAPIView.as_view(), name='public-services'),
    path('public-services/<int:pk>/', PublicServicesDetailAPIView.as_view(), name='public-services-detail'),
    path('public-company/', PublicCompanyListAPIView.as_view(), name='public-company'),
    path('public-company/<int:pk>/', PublicCompanyDetailAPIView.as_view(), name='public-company-detail'),
    path('remove-company-services/<int:pk>/', RemoveServicesAPIView.as_view(), name='remove-company-services'),
    path('remove-company-images/<int:pk>/', RemoveCompanyImagesAPIView.as_view(), name='remove-company-images'),
    path('remove-company-staff/<int:pk>/', RemoveCompanyStaffAPIView.as_view(), name='remove-company-staff'),
    path('update-company-services/<int:pk>/', UpdateCompanyServicesAPIView.as_view(), name='update-company-services'),
    path('update-company-images/<int:pk>/', UpdateCompanyImagesAPIView.as_view(), name='update-company-images'),
    path('update-company-staff/<int:pk>/', UpdateCompanyStaffAPIView.as_view(), name='update-company-staff'),

]
