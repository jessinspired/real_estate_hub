from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ApartmentForSaleViewSet, ApartmentForRentViewSet, LandViewSet, PropertyImageViewSet

router = DefaultRouter()
router.register(r'apartments-for-sale', ApartmentForSaleViewSet,
                basename='apartment-for-sale')
router.register(r'apartments-for-rent', ApartmentForRentViewSet,
                basename='apartment-for-rent')
router.register(r'lands', LandViewSet, basename='land')

router.register(r'upload_image', PropertyImageViewSet, basename='upload_image')

urlpatterns = [
    path('', include(router.urls)),
]
