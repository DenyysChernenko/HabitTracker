import random
import datetime

from django.core.management.base import BaseCommand
from habits.models import Habit
from users.models import User


class Command(BaseCommand):
    help = 'Fill DB with random habits'

    def handle(self, *args, **options):

        users = User.objects.all()

        for user in users:
            for i in range(1, 7):
                name = f'Habit {i} for {user.username}'
                description = f'Description for {name}'
                end_date = datetime.date.today() + datetime.timedelta(days=random.randint(1, 365))
                current_streak = random.randint(0, 100)
                is_completed = random.choice([True, False])

                Habit.objects.create(
                    name=name,
                    description=description,
                    user=user,
                    end_date=end_date,
                    current_streak=current_streak,
                    is_completed=is_completed
                )

        self.stdout.write(self.style.SUCCESS('Successfully filled the database with random habits.'))
