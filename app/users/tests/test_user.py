from django.test import TestCase
from django.contrib.auth import get_user_model


class UserManagerTests(TestCase):
    """test manager user"""
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='me@ngelrojasp.com',
            password='me123456'
        )
        self.assertEqual(user.email, 'me@ngelrojasp.com')
        self.assertTrue(user.is_activate)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            'admin@ngelrojasp.com',
            'admin2020'
        )
        self.assertEqual(admin_user.email, 'admin@ngelrojasp.com')
        self.assertTrue(admin_user.is_activate)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
