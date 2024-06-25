from django.db import models

# Create your models here.


class Achievement(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    requirements = models.TextField()
    reward = models.TextField()
    is_achieved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
