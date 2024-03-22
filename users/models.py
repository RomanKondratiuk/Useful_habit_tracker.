from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """ This is a users model"""
    phone = models.CharField(max_length=20, verbose_name='phone_number',
                             **NULLABLE)
    city = models.TextField(max_length=50, verbose_name='city',
                            **NULLABLE)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='avatar',
                               **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='email')
    telegram_chat_id = models.CharField(max_length=100,
                                        verbose_name='Telegram chat ID',
                                        blank=True)

    # Changing authorization from username to e-mail
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'last_name', 'telegram_chat_id']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
