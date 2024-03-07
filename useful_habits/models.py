from django.utils import timezone
from config import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator
from datetime import timedelta

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    """ the model for useful habit """
    action = models.CharField(max_length=255, verbose_name='action')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='user', **NULLABLE)

    def __str__(self):
        return f"{self.action}"

    class Meta:
        verbose_name = 'habit'
        verbose_name_plural = 'habits'


class Feeling(models.Model):
    """ self-awareness"""

    period = [
        ('week', 'once a week'),
        ('every_day', 'every day')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='user', **NULLABLE)
    place = models.CharField(max_length=255, verbose_name='place of action')
    action_time = models.TimeField(verbose_name='time of action', default=timezone.now())
    action = models.CharField(max_length=255, verbose_name='action')
    nice_feeling = models.BooleanField(default=False, verbose_name='a sign of a pleasant feeling')
    related_habit = models.ForeignKey(Habit, on_delete=models.CASCADE, verbose_name='related habit', **NULLABLE)
    frequency = models.CharField(choices=period, default='every_day', verbose_name="Periodicity")
    reward = models.CharField(max_length=255, verbose_name='reward', ** NULLABLE)
    time_to_complete = models.DurationField(verbose_name='time to complete',
                                            validators=[MaxValueValidator(timedelta(seconds=120))])
    is_public = models.BooleanField(default=True, verbose_name='sign of publicity')

    def __str__(self):
        return f"{self.action}"

    def clean(self):
        # Checking for simultaneous filling of the reward and related_habit fields
        if self.reward and self.related_habit:
            raise ValidationError(_('You cannot specify a reward and an associated habit at the same time.'))

    def save(self, *args, **kwargs):
        self.clean()
        super(Feeling, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'feeling'
        verbose_name_plural = 'feelings'


