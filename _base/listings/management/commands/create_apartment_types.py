# realestate/management/commands/create_apartment_types.py
from django.core.management.base import BaseCommand
from listings.models import ApartmentType


class Command(BaseCommand):
    help = "Create default apartment types"

    def handle(self, *args, **options):
        created_count = 0
        for type_value, type_display in ApartmentType.Type.choices:
            obj, created = ApartmentType.objects.get_or_create(name=type_value)
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(
                    f"Created: {type_display}"))
            else:
                self.stdout.write(self.style.WARNING(
                    f"Already exists: {type_display}"))

        self.stdout.write(self.style.SUCCESS(
            f"Finished! {created_count} new types created."))
