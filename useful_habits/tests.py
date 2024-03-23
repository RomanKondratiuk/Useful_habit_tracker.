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
            "owner": self.user.id,
            "place": 'home',
            "perform_time": "10:00:00",
            "action": "test action",
            "is_pleasant": False,
            "frequency": "every_day",
            "reward": "rest",
            "time_to_complete": "00:02:00",
            "is_public": True,

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
            {"id": 1,
             "owner": 1,
             "place": 'home',
             "perform_time": "10:00:00",
             "action": "test action",
             "is_pleasant": False,
             "frequency": "every_day",
             "reward": "rest",
             "time_to_complete": "00:02:00",
             "last_completed": None,
             "is_public": True,
             "linked_habit": None}
        )

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_list_habit(self):
        """ testing the list of habits """

        # checking that the habit is created only for authenticated users
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            '/habit/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {'count': 0, 'next': None, 'previous': None, 'results': []}
        )

    def test_update_habit(self):
        """ test for updating test """
        self.client.force_authenticate(user=self.user)

        habit = Habit.objects.create(
            owner=self.user,
            place='home',
            perform_time="10:00:00",
            action="initial action",
            is_pleasant=False,
            frequency="every_day",
            reward="initial reward",
            time_to_complete="00:02:00",
            is_public=True,
        )

        updated_data = {
            "action": "updated action",
            "reward": "updated reward",
        }

        response = self.client.put(
            f'/habit/update/{habit.id}/',
            data=updated_data)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK)

        habit.refresh_from_db()
        self.assertEqual(
            habit.action,
            "updated action")

        self.assertEqual(
            habit.reward,
            "updated reward")
