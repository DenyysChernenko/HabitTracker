# Generated by Django 5.0.6 on 2024-06-28 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xp_logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='xplog',
            options={'ordering': ['xp_value'], 'verbose_name': 'XpLog', 'verbose_name_plural': 'XpLogs'},
        ),
    ]
