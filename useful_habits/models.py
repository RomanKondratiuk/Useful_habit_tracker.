from config import settings
from django.db import models
from django.core.validators import MaxValueValidator
from datetime import timedelta

from useful_habits.valiators import validate_reward_and_habit, validate_pleasant_habit, \
    validate_enjoyable_habit_without_reward_or_association

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    """ the model for useful habit """
    action = models.CharField(max_length=255, verbose_name='action')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='owner', **NULLABLE)
    nice_feeling = models.BooleanField(default=False, verbose_name='a sign of a pleasant feeling')
    periodicity = models.IntegerField(default=7, verbose_name='frequency of habit execution')
    last_completed = models.DateField(verbose_name='last due date', **NULLABLE)
    is_public = models.BooleanField(default=True, verbose_name="public habits")

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
    action = models.CharField(max_length=255, verbose_name='action')
    related_habit = models.ForeignKey(Habit, on_delete=models.CASCADE, verbose_name='related habit', **NULLABLE)
    frequency = models.CharField(choices=period, default='every_day', verbose_name="Periodicity")
    reward = models.CharField(max_length=255, verbose_name='reward', **NULLABLE)
    time_to_complete = models.DurationField(verbose_name='time to complete',
                                            validators=[MaxValueValidator(timedelta(seconds=120))])

    def __str__(self):
        return f"{self.action}"

    def clean(self):
        # Checking for simultaneous filling of the reward and related_habit fields
        validate_reward_and_habit(self.reward, self.related_habit)

        # Checking that an associated habit has the sign of a pleasant habit
        validate_pleasant_habit(self.related_habit, self.related_habit.nice_feeling if self.related_habit else False)

        # Checking that enjoyable habit cannot have a reward or associated habit.
        validate_enjoyable_habit_without_reward_or_association(self.nice_feeling, self.reward, self.related_habit)

    def save(self, *args, **kwargs):
        self.clean()
        super(Feeling, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'feeling'
        verbose_name_plural = 'feelings'

