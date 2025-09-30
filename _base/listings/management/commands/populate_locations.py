# realestate/management/commands/populate_states_regions.py
from django.core.management.base import BaseCommand
from listings.models import State, Region


class Command(BaseCommand):
    help = "Populate the database with states and regions"

    def handle(self, *args, **options):
        data = {
            "Rivers": [f"Rivers Region {i+1}" for i in range(10)],
            "Abuja": [f"Abuja Region {i+1}" for i in range(10)],
            "Lagos": [f"Lagos Region {i+1}" for i in range(10)],
        }

        for state_name, regions in data.items():
            state, created = State.objects.get_or_create(name=state_name)
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f"Created State: {state_name}"))
            else:
                self.stdout.write(self.style.WARNING(
                    f"State already exists: {state_name}"))

            for region_name in regions:
                region_obj, region_created = Region.objects.get_or_create(
                    name=region_name,
                    state=state
                )
                if region_created:
                    self.stdout.write(self.style.SUCCESS(
                        f"  Created Region: {region_name}"))
                else:
                    self.stdout.write(self.style.WARNING(
                        f"  Region already exists: {region_name}"))

        self.stdout.write(self.style.SUCCESS(
            "Finished populating states and regions!"))
