from rest_framework import serializers
from .models import Habit
from useful_habits.valiators import \
    validate_linked_habit, \
    validate_reward_for_useful_habit


class HabitSerializer(serializers.ModelSerializer):
    """ serializer for habit model"""

    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        # Create a temporary instance of the Habit model
        habit = Habit(**data)

        # Calling validators
        validate_linked_habit(habit)
        validate_reward_for_useful_habit(habit)
        return data
