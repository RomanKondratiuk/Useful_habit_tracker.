from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from .models import Habit
from .services import MyBot


@shared_task
def check_habits_and_send_reminders():
    today = timezone.now().date()
    habits = Habit.objects.all()

    for habit in habits:
        if habit.last_completed is None or (today - habit.last_completed).days > habit.periodicity:
            send_reminder(habit.user, habit)


def send_reminder(user, habit):
    my_bot = MyBot()
    my_bot.send_message(f'It\'s time to perform your habit: {habit.action}. You set it to be done every {habit.periodicity} days.')


# def send_reminder(user, habit):
#     send_mail(
#         subject='Time to complete your habit!',
#         message=f'It\'s time to perform your habit: {habit.action}. You set it to be done every {habit.periodicity} days.',
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[user.email],
#         fail_silently=False
#     )
