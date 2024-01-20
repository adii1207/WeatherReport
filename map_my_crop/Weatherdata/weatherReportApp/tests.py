from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class UserRegistrationViewTests(APITestCase):
    def test_registration_success(self):
        url = reverse('user-registration')
        data = {
            'username': 'testuser',
            'password': 'testpassword123',
            'email': 'test@example.com'
        }
        # self.client.login(username='testuser', password='testpassword123')
        self.client.force_authenticate(user='testuser')
        response = self.client.post(url, data, format='json')
        print("registration success", self.assertEqual(response.status_code, status.HTTP_201_CREATED))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Logout the user after the test
        self.client.logout()
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_registration_fail(self):
        url = reverse('user-registration')
        data = {
            'username': '',  # Username is required
            'password': 'testpassword123',
            'email': 'test@example.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

class WeatherHistoricDataTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.url = reverse('weather-report-data')

    def test_access_denied_without_authentication(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
