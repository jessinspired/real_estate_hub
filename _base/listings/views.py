from rest_framework import viewsets
from .models import (
    PropertyImage,
    ApartmentForSale,
    ApartmentForRent,
    Land,
    ApartmentForRentImage,
    ApartmentForSaleImage,
    LandImage,
)
from users.permissions import IsAgentOrLandlord
from listings.serializers import (
    ApartmentForSaleSerializer,
    ApartmentForRentSerializer,
    LandSerializer,
    PropertyImageSerializer,
    ApartmentForRentImageSerializer,
    ApartmentForSaleImageSerializer,
    LandImageSerializer,
)
from rest_framework.parsers import MultiPartParser, FormParser


class ApartmentForSaleViewSet(viewsets.ModelViewSet):
    queryset = ApartmentForSale.objects.all()
    serializer_class = ApartmentForSaleSerializer
    permission_classes = [IsAgentOrLandlord]

    def perform_create(self, serializer):
        if self.request.user.is_agent:
            serializer.save(agent=self.request.user.role_instance)
        elif self.request.user.is_landlord:
            serializer.save(landlord=self.request.user.role_instance)


class ApartmentForRentViewSet(viewsets.ModelViewSet):
    queryset = ApartmentForRent.objects.all()
    serializer_class = ApartmentForRentSerializer
    permission_classes = [IsAgentOrLandlord]

    def perform_create(self, serializer):
        if self.request.user.is_agent:
            serializer.save(agent=self.request.user.role_instance)
        elif self.request.user.is_landlord:
            serializer.save(landlord=self.request.user.role_instance)


class LandViewSet(viewsets.ModelViewSet):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    permission_classes = [IsAgentOrLandlord]

    def perform_create(self, serializer):
        if self.request.user.is_agent:
            serializer.save(agent=self.request.user.role_instance)
        elif self.request.user.is_landlord:
            serializer.save(landlord=self.request.user.role_instance)


# image upload demo


class PropertyImageViewSet(viewsets.ModelViewSet):
    # for demo purposes, we are not linking this to any property model
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer
    permission_classes = [IsAgentOrLandlord]
    http_method_names = ['get', 'post', 'head', 'delete']
    parser_classes = [MultiPartParser, FormParser]


class ApartmentForRentImageViewSet(viewsets.ModelViewSet):
    queryset = ApartmentForRentImage.objects.all()
    serializer_class = ApartmentForRentImageSerializer
    permission_classes = [IsAgentOrLandlord]
    http_method_names = ['get', 'post', 'head', 'delete']
    parser_classes = [MultiPartParser, FormParser]


class ApartmentForSaleImageViewSet(viewsets.ModelViewSet):
    queryset = ApartmentForSaleImage.objects.all()
    serializer_class = ApartmentForSaleImageSerializer
    permission_classes = [IsAgentOrLandlord]
    http_method_names = ['get', 'post', 'head', 'delete']
    parser_classes = [MultiPartParser, FormParser]


class LandImageViewSet(viewsets.ModelViewSet):
    queryset = LandImage.objects.all()
    serializer_class = LandImageSerializer
    permission_classes = [IsAgentOrLandlord]
    http_method_names = ['get', 'post', 'head', 'delete']
    parser_classes = [MultiPartParser, FormParser]
