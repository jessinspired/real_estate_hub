# realestate/serializers.py
from rest_framework import serializers
from .models import ApartmentForSale, ApartmentForRent, Land

class ApartmentForSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentForSale
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]


class ApartmentForRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentForRent
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]


class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]
