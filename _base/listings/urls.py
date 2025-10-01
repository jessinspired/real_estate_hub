from rest_framework.routers import DefaultRouter
from django.urls import path, include
import listings.views as views

router = DefaultRouter()
router.register(r'apartments-for-sale', views.ApartmentForSaleViewSet,
                basename='apartment-for-sale')
router.register(r'apartments-for-rent', views.ApartmentForRentViewSet,
                basename='apartment-for-rent')
router.register(r'lands', views.LandViewSet, basename='land')


# image upload demo
router.register(r'upload_image', views.PropertyImageViewSet,
                basename='upload_image')

# image upload for apartment for rent
router.register(r'apartment-for-rent-images', views.ApartmentForRentImageViewSet,
                basename='apartment-for-rent-images')

router.register(r'apartment-for-sale-images', views.ApartmentForSaleImageViewSet,
                basename='apartment-for-sale-images')

router.register(r'land-images', views.LandImageViewSet,
                basename='land-images')

urlpatterns = [
    path('', include(router.urls)),
]
