from django.db import models
# Create your models here.


class XpLog(models.Model):

    # TODO make Source TYPE and Source ID correctly
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # habit_id = models.ForeignKey(Habit, on_delete=models.CASCADE)
    xp_value = models.IntegerField()

    def __str__(self):
        return self.xp_value
