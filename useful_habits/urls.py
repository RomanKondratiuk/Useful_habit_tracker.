from django.urls import path
from useful_habits.apps import UsefulHabitsConfig
from useful_habits.views import HabitCreateApiView, HabitListApiView, \
    HabitRetrieveApiView, HabitUpdateApiView, \
    HabitDestroyAPIView, PublicHabitListApiView

app_name = UsefulHabitsConfig.name

urlpatterns = [
    path('', PublicHabitListApiView.as_view(), name='public habit list'),
    path('habit/', HabitListApiView.as_view(), name='habit-list'),
    path('habit/<int:pk>/', HabitRetrieveApiView.as_view(),
         name='read one habit'),
    path('habit/create/', HabitCreateApiView.as_view(), name='habit-create'),
    path('habit/update/<int:pk>/', HabitUpdateApiView.as_view(),
         name='habit-update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(),
         name='habit-delete'),
]
