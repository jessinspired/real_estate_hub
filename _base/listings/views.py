from .serializers import PropertyImageSerializer
from .models import PropertyImage
from rest_framework import viewsets
from .models import ApartmentForSale, ApartmentForRent, Land
from users.permissions import IsAgentOrLandlord
from listings.serializers import ApartmentForSaleSerializer, ApartmentForRentSerializer, LandSerializer
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
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer
    permission_classes = [IsAgentOrLandlord]
    http_method_names = ['get', 'post', 'head', 'delete']
    parser_classes = [MultiPartParser, FormParser]
