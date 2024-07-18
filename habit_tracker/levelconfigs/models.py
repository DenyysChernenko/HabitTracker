from django.db import models

# Create your models here.


class LevelConfig(models.Model):
    level = models.IntegerField(unique=True)
    xp_required = models.IntegerField()

    def __str__(self):
        return f"Level {self.level}: {self.xp_required} XP"
