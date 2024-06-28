# Generated by Django 5.0.6 on 2024-06-28 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='achievement',
            options={'ordering': ['name'], 'verbose_name': 'Achievement', 'verbose_name_plural': 'Achievements'},
        ),
        migrations.AlterField(
            model_name='achievement',
            name='description',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='name',
            field=models.CharField(),
        ),
    ]
