# realestate/serializers.py
from .models import PropertyImage
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


# for image demo


class PropertyImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = PropertyImage
        fields = ["id", "image", "image_url", "uploaded_at"]
        read_only_fields = ["id", "uploaded_at"]

    def get_image_url(self, obj):
        if obj.image:
            # This uses Django Storage backend (CloudFront if set)
            return obj.image.url
        return None
