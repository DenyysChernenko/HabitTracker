import random

from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):

        for i in range(1, 10):
            username = f'Username {i}'
            email = f"malformed{i}@gmail.com"
            password = f"123123123123"
            experience = random.randint(0, 1500)
            level = random.randint(1, 134)

            User.objects.create(
                username=username,
                email=email,
                password=password,
                experience=experience,
                level=level
            )

        self.stdout.write(self.style.SUCCESS('Successfully filled database with random users'))
