from django.db import models

# Create your models here.


class Reminder(models.Model):

    time = models.DateTimeField()
    frequency = models.IntegerField()
    message = models.CharField(max_length=120)

    def __str__(self):
        return self.message
