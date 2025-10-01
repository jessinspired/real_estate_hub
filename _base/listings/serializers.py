# realestate/serializers.py
from rest_framework import serializers
from .models import (
    PropertyImage,
    ApartmentForSale,
    ApartmentForRent,
    Land,
    ApartmentForRentImage,
    ApartmentForSaleImage,
    LandImage,
)


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


# Listing images serializers
class PropertyImageSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField()

    class Meta:
        model = PropertyImage
        fields = ["id", "image", "uploaded_at"]
        read_only_fields = ["id", "uploaded_at"]

    # def get_image_url(self, obj):
    #     if obj.image:
    #         # This uses Django Storage backend (CloudFront if set)
    #         return obj.image.url
    #     return None


class ApartmentForRentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentForRentImage
        fields = ["id", "image", "apartment_for_rent", "uploaded_at"]
        read_only_fields = ["id", "uploaded_at"]


class ApartmentForSaleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentForSaleImage
        fields = ["id", "image", "apartment_for_sale", "uploaded_at"]
        read_only_fields = ["id", "uploaded_at"]


class LandImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandImage
        fields = ["id", "image", "land", "uploaded_at"]
        read_only_fields = ["id", "uploaded_at"]
