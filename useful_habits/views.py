from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from useful_habits.models import Habit, Feeling
from useful_habits.paginators import HabitPaginator
from useful_habits.permissions import IsOwner
from useful_habits.serializer import HabitSerializer, FeelingSerializer


class HabitCreateApiView(generics.CreateAPIView):
    """ creating a habit """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitListApiView(generics.ListAPIView):
    """ list of habits """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator


class HabitRetrieveApiView(generics.RetrieveAPIView):
    """ reading of  one habit """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]


class HabitUpdateApiView(generics.UpdateAPIView):
    """ updating a habit """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ deleting of habits """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]



class FeelingCreateApiView(generics.CreateAPIView):
    """ creating a feeling """
    serializer_class = FeelingSerializer
    queryset = Feeling.objects.all()
    permission_classes = [IsOwner]


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
    permission_classes = [IsOwner]


class FeelingDestroyAPIView(generics.DestroyAPIView):
    """ deleting of feeling """
    serializer_class = FeelingSerializer
    queryset = Feeling.objects.all()
    permission_classes = [IsOwner]

