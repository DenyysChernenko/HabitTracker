# Generated by Django 5.0.6 on 2024-07-13 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0004_remove_habit_profile_picture_habit_habit_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='habit',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
