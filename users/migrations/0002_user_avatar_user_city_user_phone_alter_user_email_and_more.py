# Generated by Django 5.0.3 on 2024-03-07 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='avatar'),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='city'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='phone_number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='last_name'),
        ),
    ]
