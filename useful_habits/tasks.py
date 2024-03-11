from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config import settings
from .models import Habit
from .services import send_telegram_message


@shared_task
def check_habits_and_send_reminders():
    """checking whether the habit execution period has expired"""
    today = timezone.now().date()
    habits = Habit.objects.all()

    for habit in habits:
        if habit.last_completed is None or (today - habit.last_completed).days > habit.periodicity:
            send_email_reminder(habit.user, habit)
            send_telegram_reminder(habit.user, habit)


def send_email_reminder(user, habit):
    """ sending email """
    send_mail(
        subject='Time to complete your habit!',
        message=f'It\'s time to perform your habit: {habit.action}. You set it to be done every {habit.periodicity} days.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False,
    )


def send_telegram_reminder(user, habit):
    """sending telegram message"""
    if user.telegram_chat_id:
        message = f'It\'s time to perform your habit: {habit.action}. You set it to be done every {habit.periodicity} days.'
        send_telegram_message(user.telegram_chat_id, message)