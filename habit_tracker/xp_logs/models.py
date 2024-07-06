from django.db import models
# Create your models here.


class XpLog(models.Model):

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    habit = models.ForeignKey('habits.Habit', on_delete=models.CASCADE)
    source_type = models.CharField(20)
    xp_value = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.xp_value)

    class Meta:

        verbose_name = 'XpLog'
        verbose_name_plural = 'XpLogs'
        ordering = ['xp_value']
