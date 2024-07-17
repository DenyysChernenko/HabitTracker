from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    objects = UserManager()

    experience = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"User with username: '{self.username}' and level: '{self.level}'"

    class Meta:

        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['username']

