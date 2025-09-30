# realestate/views.py
from rest_framework import viewsets
from .models import ApartmentForSale, ApartmentForRent, Land
from users.permissions import IsAgentOrLandlord, IsOwnerOrReadOnly
from listings.serializers import ApartmentForSaleSerializer, ApartmentForRentSerializer, LandSerializer


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
            serializer.save(agent=self.request.user.agent)
        elif self.request.user.is_landlord:
            serializer.save(landlord=self.request.user.landlord)


class LandViewSet(viewsets.ModelViewSet):
    queryset = Land.objects.all()
    serializer_class = LandSerializer
    permission_classes = [IsAgentOrLandlord]

    def perform_create(self, serializer):
        if self.request.user.is_agent:
            serializer.save(agent=self.request.user.agent)
        elif self.request.user.is_landlord:
            serializer.save(landlord=self.request.user.landlord)
