from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from useful_habits.models import Habit, Feeling
from useful_habits.paginators import HabitPaginator
from useful_habits.permissions import IsOwner
from useful_habits.serializer import HabitSerializer, FeelingSerializer


class PublicHabitListApiView(generics.ListAPIView):
    """ list of public habits """
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitCreateApiView(generics.CreateAPIView):
    """ creating a habit """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]


class HabitListApiView(generics.ListAPIView):
    """ list of habits """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(owner=user)


class HabitRetrieveApiView(generics.RetrieveAPIView):
    """ reading of  one habit """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


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
    permission_classes = [IsAuthenticated]


class FeelingListApiView(generics.ListAPIView):
    """ list of feelings """
    serializer_class = FeelingSerializer
    queryset = Feeling.objects.all()
    permission_classes = [IsAuthenticated]


class FeelingRetrieveApiView(generics.RetrieveAPIView):
    """ reading of  one feeling """
    serializer_class = FeelingSerializer
    queryset = Feeling.objects.all()
    permission_classes = [IsOwner]


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
