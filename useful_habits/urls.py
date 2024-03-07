from django.db import router
from django.urls import path
from rest_framework.routers import DefaultRouter

from useful_habits.apps import UsefulHabitsConfig
from useful_habits.views import HabitCreateApiView, HabitListApiView, HabitRetrieveApiView, HabitUpdateApiView, \
    HabitDestroyAPIView

app_name = UsefulHabitsConfig.name

urlpatterns = [
    path('', HabitListApiView.as_view(), name='habit-create'),
    path('habit/<int:pk>/', HabitRetrieveApiView.as_view(), name='retrieve one habit'),
    path('habit/create/', HabitCreateApiView.as_view(), name='habit-create'),
    path('habit/update/<int:pk>/', HabitUpdateApiView.as_view(), name='habit-update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-delete'),
]
