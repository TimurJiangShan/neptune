from django.test import TestCase

# Create your tests here.

# API Test cases
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from Archive.apps.user_operation.models import Users_Operation

class UsersTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('users-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Users_Operation.objects.count(), 1)
        self.assertEqual(Users_Operation.objects.get().name, 'DabApps')