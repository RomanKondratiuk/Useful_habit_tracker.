from config import settings
from django.db import models
from django.core.validators import MaxValueValidator
from datetime import timedelta, time

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    """ the model for useful habit """
    period = [
        ('week', 'once a week'),
        ('every_day', 'every day')
    ]
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='owner', **NULLABLE)
    place = models.CharField(max_length=255, verbose_name='place of action', **NULLABLE)
    perform_time = models.TimeField(verbose_name='Time to perform the habit', default=time(10, 0))
    action = models.CharField(max_length=255, verbose_name='action')
    is_pleasant = models.BooleanField(default=False, verbose_name='Is a pleasant habit?')
    linked_habit = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE,
                                     related_name='related_habits', verbose_name='Linked Habit')
    frequency = models.CharField(choices=period, default='every_day', verbose_name="Periodicity")
    reward = models.CharField(max_length=255, verbose_name='reward', **NULLABLE)
    time_to_complete = models.DurationField(verbose_name='time to complete', **NULLABLE,
                                            validators=[MaxValueValidator(timedelta(seconds=120))])
    last_completed = models.DateField(verbose_name='last due date', **NULLABLE)
    is_public = models.BooleanField(default=True, verbose_name="public habits")

    def __str__(self):
        return f"{self.action}"

    class Meta:
        verbose_name = 'habit'
        verbose_name_plural = 'habits'
        ordering = ['place']
