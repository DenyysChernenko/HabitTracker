from django.db import models

# Create your models here.


class User(models.Model):

    # TODO correct handling password attribute
    username = models.CharField(max_length=55)
    email = models.EmailField()
    password = models.CharField()
    experience = models.IntegerField()
    level = models.IntegerField()

    def __str__(self):
        return f"User with username: '{self.username}' and level: '{self.level}'"

