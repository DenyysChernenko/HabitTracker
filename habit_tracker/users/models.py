from django.db import models

# Create your models here.


class User(models.Model):

    username = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    password = models.CharField()
    experience = models.IntegerField(default=0)
    level = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User with username: '{self.username}' and level: '{self.level}'"

