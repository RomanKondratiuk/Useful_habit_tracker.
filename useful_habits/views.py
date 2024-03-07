from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from useful_habits.models import Habit
from useful_habits.serializer import HabitSerializer


class HabitCreateApiView(generics.CreateAPIView):
    """ creating a habit """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [AllowAny]


class HabitListApiView(generics.ListAPIView):
    """ list of habits """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [AllowAny]


class HabitRetrieveApiView(generics.RetrieveAPIView):
    """ reading of  one habit """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [AllowAny]


class HabitUpdateApiView(generics.UpdateAPIView):
    """ updating a habit """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [AllowAny]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ deleting of habits """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [AllowAny]

