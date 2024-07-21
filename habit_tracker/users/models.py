from django.db import models
from django.urls import reverse
from levelconfigs.models import LevelConfig
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, username, email, first_name=None, last_name=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('last_name', 'User')
        extra_fields.setdefault('first_name', 'Admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password=password, **extra_fields)


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

    def get_progress_percentage(self):
        try:
            current_level_config = LevelConfig.objects.get(level=self.level)
            next_level_config = LevelConfig.objects.get(level=self.level + 1)
            current_xp = self.experience - current_level_config.xp_required if self.level > 1 else self.experience
            required_xp = next_level_config.xp_required - current_level_config.xp_required
            progress = (current_xp / required_xp) * 100
            return min(progress, 100)
        except LevelConfig.DoesNotExist:
            return 100

    class Meta:

        verbose_name = 'User'
        verbose_name_plural = 'Users'

