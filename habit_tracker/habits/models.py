from django.db import models

# Create your models here.


class Habit(models.Model):

    name = models.CharField()
    description = models.CharField(blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    end_date = models.DateTimeField()
    current_streak = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Habit: {self.name} with description: {self.description}, current has streak: {self.current_streak}"

    class Meta:

        verbose_name = 'Habit'
        verbose_name_plural = 'Habits'
        ordering = ['name']
