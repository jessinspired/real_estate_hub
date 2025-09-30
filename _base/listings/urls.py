from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ApartmentForSaleViewSet, ApartmentForRentViewSet, LandViewSet

router = DefaultRouter()
router.register(r'apartments-for-sale', ApartmentForSaleViewSet, basename='apartment-for-sale')
router.register(r'apartments-for-rent', ApartmentForRentViewSet, basename='apartment-for-rent')
router.register(r'lands', LandViewSet, basename='land')

urlpatterns = [
    path('', include(router.urls)),
]
