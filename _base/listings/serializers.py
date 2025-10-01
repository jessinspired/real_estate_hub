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

# media files serializers


class GenericImageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        fields = ["id", "url"]

    def get_url(self, obj):
        return obj.image.url


class ApartmentForRentImageSerializer(GenericImageSerializer):
    class Meta:
        model = ApartmentForRentImage
        fields = ["id", "image", "apartment_for_rent", "uploaded_at"]
        read_only_fields = ["id", "uploaded_at"]


class ApartmentForSaleImageSerializer(GenericImageSerializer):
    class Meta:
        model = ApartmentForSaleImage
        fields = ["id", "image", "apartment_for_sale", "uploaded_at"]
        read_only_fields = ["id", "uploaded_at"]


class LandImageSerializer(GenericImageSerializer):
    class Meta:
        model = LandImage
        fields = ["id", "image", "land", "uploaded_at"]
        read_only_fields = ["id", "uploaded_at"]


# property serializers
class ApartmentForSaleSerializer(serializers.ModelSerializer):
    images = ApartmentForSaleImageSerializer(many=True, read_only=True)

    class Meta:
        model = ApartmentForSale
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]


class ApartmentForRentSerializer(serializers.ModelSerializer):
    images = ApartmentForRentImageSerializer(many=True, read_only=True)

    class Meta:
        model = ApartmentForRent
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]


class LandSerializer(serializers.ModelSerializer):
    images = LandImageSerializer(many=True, read_only=True)

    class Meta:
        model = Land
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]


# for demo
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
