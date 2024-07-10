
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CompanyViewSet, RemoveCompanyServicesAPIView,
    RemoveCompanyImagesAPIView, RemoveCompanyStaffAPIView,
    UpdateCompanyServicesAPIView, UpdateCompanyImagesAPIView, UpdateCompanyStaffAPIView,
)


router = DefaultRouter()
router.register('company', CompanyViewSet, basename='company')


urlpatterns = [
    path('', include(router.urls)),
    path('remove-company-services/<int:pk>/', RemoveCompanyServicesAPIView.as_view(), name='remove-company-services'),
    path('remove-company-images/<int:pk>/', RemoveCompanyImagesAPIView.as_view(), name='remove-company-images'),
    path('remove-company-staff/<int:pk>/', RemoveCompanyStaffAPIView.as_view(), name='remove-company-staff'),
    path('update-company-services/<int:pk>/', UpdateCompanyServicesAPIView.as_view(), name='update-company-services'),
    path('update-company-images/<int:pk>/', UpdateCompanyImagesAPIView.as_view(), name='update-company-images'),
    path('update-company-staff/<int:pk>/', UpdateCompanyStaffAPIView.as_view(), name='update-company-staff'),

]
