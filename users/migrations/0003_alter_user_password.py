# Generated by Django 5.0.3 on 2024-03-07 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_avatar_user_city_user_phone_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.IntegerField(max_length=50, verbose_name='password'),
        ),
    ]
