from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_linked_habit(habit):
    if habit.is_pleasant and habit.linked_habit is not None:
        raise ValidationError(_('Pleasant habits cannot have a linked habit.'))


def validate_reward_for_useful_habit(habit):
    if not habit.is_pleasant and habit.reward:
        raise ValidationError(_('Only useful habits can have a reward.'))
