from django.core.management.base import BaseCommand
from flow_app.tasks import generate_flow_data

class Command(BaseCommand):
    help = 'Generates flow data'

    def handle(self, *args, **options):
        daily_flow, total_flow = generate_flow_data()
        self.stdout.write(self.style.SUCCESS(
            f'Successfully generated flow data. Daily: {daily_flow}, Total: {total_flow}'
        ))