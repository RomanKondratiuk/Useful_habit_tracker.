from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_reward_and_habit(reward, related_habit):
    """Checking for simultaneous filling
    of the reward and related_habit fields"""
    if reward and related_habit:
        raise ValidationError(_('You cannot specify a reward and an '
                                'associated habit at the same time.'))


def validate_pleasant_habit(related_habit, nice_feeling):
    """Checking that an associated habit has the sign of a pleasant habit"""
    if related_habit and not nice_feeling:
        raise ValidationError(_('Associated habits can only be those with the'
                                ' characteristic of a pleasant habit.'))


def validate_enjoyable_habit_without_reward_or_association(
        nice_feeling, reward, related_habit):

    """Checking that enjoyable habit cannot have
    a reward or associated habit."""

    if nice_feeling and not (reward or related_habit):
        raise ValidationError(_('An enjoyable habit cannot have'
                                ' a reward or an associated habit.'))
