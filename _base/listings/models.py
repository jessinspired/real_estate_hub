from django.db import models
from core.models import BaseModel, StringNormalizationMixin
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


class State(StringNormalizationMixin, BaseModel):
    name = models.CharField(max_length=150)

    normalized_name = models.CharField(
        max_length=255, editable=False, null=True)

    normalized_capital_name = models.CharField(
        max_length=255, editable=False, null=True)

    capital_name = models.CharField(
        max_length=255, null=True)

    def __str__(self):
        return self.name


class Region(StringNormalizationMixin, BaseModel):
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
