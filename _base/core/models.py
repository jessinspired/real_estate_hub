from django.db import models
from django.db import models
from django.utils import timezone
import uuid
from core.utils import normalize_text


class BaseModel(models.Model):
    '''
    Basemodel class
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TextNormalizationMixin:
    def normalize_fields(self):
        self.normalized_name = normalize_text(self.name)
        if hasattr(self, "abbr"):
            self.normalized_abbr = normalize_text(
                getattr(self, "abbr", "") or "")

    def save(self, *args, **kwargs):
        # Check if this is an update (existing object)
        if self.pk:
            # Use `only()` to limit the fields fetched
            fields_to_check = ['name']

            # Add 'abbr' to the list of fields to check only if the model has the 'abbr' field
            if hasattr(self, 'abbr'):
                fields_to_check.append('abbr')

            orig = type(self).objects.filter(
                pk=self.pk).only(*fields_to_check).first()

            if orig:
                # Check if name has changed
                if orig.name != self.name:
                    self.normalized_name = normalize_text(self.name)
                # If `name` hasn't changed, check if `normalized_name` is None
                elif self.normalized_name is None:
                    self.normalized_name = normalize_text(self.name)

                # Check if abbr has changed, but only if it exists on the model
                if hasattr(self, 'abbr') and orig.abbr != getattr(self, 'abbr', None):
                    self.normalized_abbr = normalize_text(
                        getattr(self, 'abbr', '') or "")
                # If `abbr` hasn't changed, check if `normalized_abbr` is None
                elif hasattr(self, 'abbr') and self.normalized_abbr is None:
                    self.normalized_abbr = normalize_text(
                        getattr(self, 'abbr', '') or "")
        else:
            # New object, always normalize
            self.normalize_fields()

        super().save(*args, **kwargs)
