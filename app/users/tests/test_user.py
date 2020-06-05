from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIRequestFactory

# URL_USER_DETAILS = reverse("user:user-details", (), {"pk": 2})
URL_CREATE_USER = reverse("user:create")


class UserManagerTests(TestCase):
    """test manager user"""

    def setUp(self):
        self.factory = APIRequestFactory()

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="me@ngelrojasp.com", password="me123456")
        self.assertEqual(user.email, "me@ngelrojasp.com")
        self.assertTrue(user.is_activate)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser("admin@ngelrojasp.com", "admin2020")
        self.assertEqual(admin_user.email, "admin@ngelrojasp.com")
        self.assertTrue(admin_user.is_activate)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_create_user_end_point(self):
        """create user using end-point"""
        payload = {
            "first_name": "ngel",
            "last_name": "rojas",
            "email": "me@ngelrojasp.com",
            "password": "me123456",
        }
        request = self.client.post(URL_CREATE_USER, payload, format="json")
        self.assertEqual(request.status_code, 201)

    def test_retrieve_user(self):
        """retrieve current user"""
        User = get_user_model()
        user = User.objects.create_user(email="me@ngelrojasp.com", password="me123456")
        url = reverse("user-details", (), {"pk": user.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
