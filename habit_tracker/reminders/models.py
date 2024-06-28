from django.db import models

# Create your models here.


class Reminder(models.Model):

    time = models.DateTimeField()
    frequency = models.IntegerField()
    habit = models.ForeignKey('habits.Habit', on_delete=models.CASCADE)
    message = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reminder for Habit: {self.habit.name} - {self.message}"

    class Meta:

        verbose_name = 'Reminder'
        verbose_name_plural = 'Reminders'
        ordering = ['time']
