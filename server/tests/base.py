from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APITestCase, APIClient


class BaseConfiguration(APITestCase):
    def setUp(self):
        super().setUp()
        self.client = APIClient()

        self.user1 = {
            "user": {
                "email": "arkafuuma@gmail.com",
                "phone_number": "0788088831",
                "password": "#kafuuma10#"
            }
        }
