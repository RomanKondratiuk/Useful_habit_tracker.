from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from useful_habits.models import Habit, Feeling
from useful_habits.paginators import HabitPaginator
from useful_habits.serializer import HabitSerializer, FeelingSerializer


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
    pagination_class = HabitPaginator


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



class FeelingCreateApiView(generics.CreateAPIView):
    """ creating a feeling """
    serializer_class = FeelingSerializer
    queryset = Feeling.objects.all()
    permission_classes = [AllowAny]


class FeelingListApiView(generics.ListAPIView):
    """ list of feelings """
    serializer_class = FeelingSerializer
    queryset = Feeling.objects.all()
    permission_classes = [AllowAny]


class FeelingRetrieveApiView(generics.RetrieveAPIView):
    """ reading of  one feeling """
    serializer_class = FeelingSerializer
    queryset = Feeling.objects.all()
    permission_classes = [AllowAny]


class FeelingUpdateApiView(generics.UpdateAPIView):
    """ updating a feeling """
    serializer_class = FeelingSerializer
    queryset = Feeling.objects.all()
    permission_classes = [AllowAny]


class FeelingDestroyAPIView(generics.DestroyAPIView):
    """ deleting of feeling """
    serializer_class = FeelingSerializer
    queryset = Feeling.objects.all()
    permission_classes = [AllowAny]

