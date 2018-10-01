from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from .models import Weight

username = 'user1'
password = 'password1'

class ViewTests(TestCase):
    pass

    def setUp(self):
        # Create users
        u1 = User.objects.create_user(username=username, password=password)
        self.assertIsNotNone(u1)

        # Create weights
        w1 = Weight.objects.create(date=timezone.now(), weight=200, user=u1)
        self.assertIsNotNone(w1)

    def test_user(self):
        self.assertEqual(User.objects.count(), 1)

        # Not logged in
        # response = self.client.get(reverse('weights'))
        # self.assertEqual(response.status_code, 302)

        # @login_required
        login = self.client.login(username=username, password=password)
        self.assertIsNotNone(login)
        response = self.client.get(reverse('catalog:weights'))
        self.assertEqual(response.status_code, 200)
