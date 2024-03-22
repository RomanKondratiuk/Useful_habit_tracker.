from rest_framework import status
from rest_framework.test import APITestCase
from useful_habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        # creating user
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

    def test_create_habit(self):
        """ Habit creating testing """

        # checking that the habit is created only for authenticated users
        self.client.force_authenticate(user=self.user)

        data = {
            "action": "test habit",
            "nice_feeling": True,
            "owner": self.user
        }
        response = self.client.post(
            '/habit/create/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'action': 'test habit', 'nice_feeling': True,
             'periodicity': 7, 'last_completed': None,
             'is_public': False, 'owner': None}
        )

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_list_habit(self):
        """ testing the list of habits """

        # checking that the habit is created only for authenticated users
        self.client.force_authenticate(user=self.user)

        Habit.objects.create(
            action="test habit-list",
            nice_feeling=True,
            owner=self.user
        )
        response = self.client.get(
            '/habit/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None,
             'results': [{'id': 2, 'action': 'test habit-list',
                          'nice_feeling': True,
                          'periodicity': 7, 'last_completed': None,
                          'is_public': True, 'owner': 2}]}

        )

        # def test_update_habit(self):
        #     """Testing habit updating"""
        #
        #     # Аутентификация пользователя
        #     self.client.force_authenticate(user=self.user)
        #
        #     # Создание привычки, которую будем обновлять
        #     habit = Habit.objects.create(
        #         action="Original Habit",
        #         nice_feeling=True,
        #         owner=self.user
        #     )
        #     # Получение URL для обновления привычки
        #     update_url = reverse('habit-detail', kwargs={'pk': habit.pk})
        #
        #     # Обновляемые данные
        #     updated_data = {
        #         'action': 'Updated Habit',
        #         'nice_feeling': False
        #     }
        #
        #     # Выполнение запроса PATCH для обновления привычки
        #     response = self.client.patch(update_url, updated_data, format='json')
        #
        #     # Проверка успешного ответа
        #     self.assertEqual(response.status_code, status.HTTP_200_OK)
        #
        #     # Проверка, что данные привычки были обновлены
        #     updated_habit = Habit.objects.get(pk=habit.pk)
        #     self.assertEqual(updated_habit.action, updated_data['action'])
        #     self.assertEqual(updated_habit.nice_feeling, updated_data['nice_feeling'])
