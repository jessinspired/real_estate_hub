from django.db import models
from core.models import BaseModel, TextNormalizationMixin
from django.core.exceptions import ValidationError


class ApartmentType(BaseModel):
    class Type(models.TextChoices):
        ONE_ROOM = 'one_room', 'One Room'
        SELF_CONTAINED = 'self_contained', 'Self Contained'
        ONE_BEDROOM = 'one_bedroom', 'One Bedroom'
        TWO_BEDROOMS = 'two_bedrooms', 'Two Bedrooms'
        THREE_BEDROOMS = 'three_bedrooms', 'Three Bedrooms'

    name = models.CharField(
        max_length=150,
        choices=Type.choices,
        default=None
    )

    def __str__(self):
        return self.get_name_display()

    def clean(self):
        if self.name not in ApartmentType.Type.values:
            e = f"Apartment Type - '{self.name}' is not valid"
            raise ValidationError(e)


# Regional Models
class State(TextNormalizationMixin, BaseModel):
    name = models.CharField(max_length=150)

    normalized_name = models.CharField(
        max_length=255, editable=False, null=True)

    normalized_capital_name = models.CharField(
        max_length=255, editable=False, null=True)

    capital_name = models.CharField(
        max_length=255, null=True)

    def __str__(self):
        return self.name


class Region(TextNormalizationMixin, BaseModel):
    name = models.CharField(max_length=150)

    normalized_name = models.CharField(
        max_length=255, editable=False, null=True, default=None)

    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name='regions',
        default=None
    )

    def __str__(self):
        return self.name


# Listings Models
class ApartmentForSale(BaseModel):
    price = models.DecimalField(max_digits=12, decimal_places=2)

    region = models.ForeignKey(
        Region,
        on_delete=models.PROTECT,
        related_name="apartments_for_sale"
    )
    state = models.ForeignKey(
        State,
        on_delete=models.PROTECT,
        related_name="apartments_for_sale"
    )

    apartment_type = models.ForeignKey(
        "ApartmentType",
        on_delete=models.PROTECT,
        related_name="apartments_for_sale",
    )

    agent = models.ForeignKey(
        "users.Agent",
        on_delete=models.SET_NULL,
        related_name="apartments_for_sale_by_agent",
        null=True,
        blank=True
    )

    landlord = models.ForeignKey(
        "users.Landlord",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="apartments_for_sale_by_landlord"
    )


class ApartmentForRent(BaseModel):
    rent = models.DecimalField(max_digits=12, decimal_places=2)
    initial_rent = models.DecimalField(max_digits=12, decimal_places=2)

    apartment_type = models.ForeignKey(
        "ApartmentType",
        on_delete=models.PROTECT,
        related_name="apartments_for_rent"
    )

    region = models.ForeignKey(
        Region,
        on_delete=models.PROTECT,
        related_name="apartments_for_rent"
    )

    state = models.ForeignKey(
        State,
        on_delete=models.PROTECT,
        related_name="apartments_for_rent"
    )

    agent = models.ForeignKey(
        "users.Agent",
        on_delete=models.SET_NULL,
        related_name="apartments_for_rent_by_agent",
        null=True,
        blank=True
    )

    landlord = models.ForeignKey(
        "users.Landlord",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="apartments_for_rent_by_landlord"
    )


class Land(BaseModel):
    price = models.DecimalField(max_digits=12, decimal_places=2)
    plot_size = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Size in square meters")
    titled = models.BooleanField(default=False)
    region = models.ForeignKey(
        Region,
        on_delete=models.PROTECT,
        related_name="lands"
    )
    state = models.ForeignKey(
        State,
        on_delete=models.PROTECT,
        related_name="lands"
    )

    agent = models.ForeignKey(
        "users.Agent",
        on_delete=models.SET_NULL,
        related_name="lands_for_sale_by_agent",
        null=True,
        blank=True
    )

    landlord = models.ForeignKey(
        "users.Landlord",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="lands_for_sale_by_landlord"
    )


# property images
class PropertyImage(models.Model):
    # for demo purposes, we are not linking this to any property model
    image = models.ImageField(upload_to="properties/")
    uploaded_at = models.DateTimeField(auto_now_add=True)


class ApartmentForRentImage(BaseModel):
    image = models.ImageField(upload_to="apartments_for_rent/")
    apartment_for_rent = models.ForeignKey(
        ApartmentForRent,
        on_delete=models.CASCADE,
        related_name="images"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)


class ApartmentForSaleImage(BaseModel):
    image = models.ImageField(upload_to="apartments_for_sale/")
    apartment_for_sale = models.ForeignKey(
        ApartmentForSale,
        on_delete=models.CASCADE,
        related_name="images"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)


class LandImage(BaseModel):
    image = models.ImageField(upload_to="lands/")
    land = models.ForeignKey(
        Land,
        on_delete=models.CASCADE,
        related_name="images"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
