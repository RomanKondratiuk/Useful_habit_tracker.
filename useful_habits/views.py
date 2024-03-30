from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from useful_habits.models import Habit
from useful_habits.paginators import HabitPaginator
from useful_habits.permissions import IsOwner
from useful_habits.serializer import HabitSerializer


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
