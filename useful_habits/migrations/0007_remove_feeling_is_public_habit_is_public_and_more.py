# Generated by Django 5.0.3 on 2024-03-10 04:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useful_habits', '0006_remove_habit_user_habit_owner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feeling',
            name='is_public',
        ),
        migrations.AddField(
            model_name='habit',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='public habits'),
        ),
        migrations.AlterField(
            model_name='feeling',
            name='action_time',
            field=models.TimeField(default=datetime.datetime(2024, 3, 10, 4, 23, 26, 866449, tzinfo=datetime.timezone.utc), verbose_name='time of action'),
        ),
    ]