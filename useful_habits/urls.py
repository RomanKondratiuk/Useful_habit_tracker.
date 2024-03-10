from django.urls import path

from useful_habits.apps import UsefulHabitsConfig
from useful_habits.views import HabitCreateApiView, HabitListApiView, HabitRetrieveApiView, HabitUpdateApiView, \
    HabitDestroyAPIView, FeelingListApiView, FeelingRetrieveApiView, FeelingCreateApiView, FeelingUpdateApiView, \
    FeelingDestroyAPIView, PublicHabitListApiView

app_name = UsefulHabitsConfig.name

urlpatterns = [
    path('', PublicHabitListApiView.as_view(), name='public habit list'),
    path('habit/', HabitListApiView.as_view(), name='habit-list'),
    path('habit/<int:pk>/', HabitRetrieveApiView.as_view(), name='read one habit'),
    path('habit/create/', HabitCreateApiView.as_view(), name='habit-create'),
    path('habit/update/<int:pk>/', HabitUpdateApiView.as_view(), name='habit-update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-delete'),

    path('feeling', FeelingListApiView.as_view(), name='feeling-list'),
    path('feeling/<int:pk>/', FeelingRetrieveApiView.as_view(), name='read one feeling'),
    path('feeling/create/', FeelingCreateApiView.as_view(), name='feeling-create'),
    path('feeling/update/<int:pk>/', FeelingUpdateApiView.as_view(), name='feeling-update'),
    path('feeling/delete/<int:pk>/', FeelingDestroyAPIView.as_view(), name='feeling-delete'),
]
