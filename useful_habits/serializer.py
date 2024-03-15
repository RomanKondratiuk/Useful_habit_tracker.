from rest_framework import serializers
from .models import Habit, Feeling


class HabitSerializer(serializers.ModelSerializer):
    """ serializer for habit model"""

    class Meta:
        model = Habit
        fields = '__all__'


class FeelingSerializer(serializers.ModelSerializer):
    """ serializer for Feeling model"""

    # changing time and date format for field 'action_time' in Feeling model
    action_datatime = serializers.DateTimeField(
        format="%d-%m-%Y %H:%M", read_only=True)

    class Meta:
        model = Feeling
        fields = '__all__'
