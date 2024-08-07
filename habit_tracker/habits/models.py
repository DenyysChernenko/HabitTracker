from django.db import models
from django.urls import reverse
from habit_tracker import settings

# Create your models here.


class Habit(models.Model):

    name = models.CharField()
    description = models.CharField(blank=True, null=True)
    start_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    end_date = models.DateField()
    habit_picture = models.ImageField(upload_to='habit_pics/', null=True, blank=True)
    current_streak = models.IntegerField(default=0)
    required_count = models.IntegerField(default=1)
    current_count = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('habit_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"Habit: {self.name} with description: {self.description}, current has streak: {self.current_streak}"

    class Meta:

        verbose_name = 'Habit'
        verbose_name_plural = 'Habits'
        ordering = ['name']

    def update_count(self):
        if self.current_count >= self.required_count:
            self.is_completed = True
        else:
            self.is_completed = False
        self.save()
