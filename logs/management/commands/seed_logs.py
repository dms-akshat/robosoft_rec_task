from django.core.management.base import BaseCommand
from logs.models import Log
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = "Seed the database with sample logs"

    def handle(self, *args, **kwargs):
        statuses = ['success', 'failure', 'pending']
        for _ in range(100):
            Log.objects.create(
                phone=fake.phone_number(),
                endpoint=fake.url(),
                status=random.choice(statuses),
                error_message=fake.sentence() if random.choice([True, False]) else ""
            )
        self.stdout.write(self.style.SUCCESS("Successfully seeded logs data!"))
