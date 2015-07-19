from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client


class BlogTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.blogger = User.objects.create_superuser(
            username='blogger',
            password='blogger',
            email='a@a.com',
            first_name='Epic',
            last_name='Blogger'
        )
        self.client.login(username='blogger', password='blogger')

    # Test user login
    def test_user_login(self):
        self.client.logout()
        # Incorrect test case
        data = {
            'username': 'Incorrect',
            'password': 'Incorrect'
        }
        r = self.client.post(reverse('user:login'), data=data)
        self.assertContains(r, 'Please enter a correct username and password. '
                               'Note that both fields may be case-sensitive.')

        # Correct test case
        data2 = {
            'username': 'blogger',
            'password': 'blogger'
        }
        r = self.client.post(reverse('user:login'), data=data2)
        self.assertRedirects(r, reverse('blog:list'))

    # Test user logout
    def test_user_logout(self):
        self.assertIsNotNone(self.client.session.get('_auth_user_id', None))
        self.client.get(reverse('user:logout'))
        self.assertIsNone(self.client.session.get('_auth_user_id', None))

    # Test user registration
    def test_user_registration(self):
        self.assertEqual(User.objects.count(), 1)
        self.client.logout()

        # Incorrect test case
        data = {
            'username': '',
            'password': '',
            'first_name': '',
            'last_name': '',
        }
        self.client.post(reverse('user:register'), data=data)
        self.assertEqual(User.objects.count(), 1)

        # Correct test case
        data = {
            'username': 'blogger2',
            'password': 'blogger2',
            'first_name': 'blogger2',
            'last_name': 'blogger2',
        }
        r = self.client.post(reverse('user:register'), data=data)
        self.assertRedirects(r, reverse('user:login'))
        self.assertEqual(User.objects.count(), 2)
