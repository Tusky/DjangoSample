from django.test import TestCase, Client


class BlogTest(TestCase):
    def setUp(self):
        self.client = Client()
        # TODO: Create a user
        # TODO: Create 10 blog posts
        # TODO: Create 10 blog post

    # TODO: Test if blog list page loads up, has paginator
    # TODO: Test if blog detail page loads up, has every content
