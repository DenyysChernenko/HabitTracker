# Generated by Django 5.0.6 on 2024-07-06 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_habit_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='habit',
            name='habit_picture',
            field=models.ImageField(blank=True, null=True, upload_to='habit_pics/'),
        ),
    ]
