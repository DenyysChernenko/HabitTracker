from django.db import models

# Create your models here.


class Habit(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    current_streak = models.IntegerField()
    is_completed = models.BooleanField()

    def __str__(self):
        return f"Habit: {self.name} with description: {self.description}, current has streak: {self.current_streak}"
