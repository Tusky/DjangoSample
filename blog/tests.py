from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from blog.models import Post


class BlogTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.blogger = User.objects.create(username='blogger', password='blogger')
        self.client.login(username='blogger', password='blogger')
        for i in range(10):
            Post.objects.create(
                title='Epic title %d' % i,
                content='This is the content for Epic title %d' % i,
                posted_by=self.blogger
            )

    # Test if model's __str__ returns the correct details.
    def test_model_str(self):
        post = Post.objects.latest('pk')
        self.assertEqual(post.__str__(), "%s by %s" % (post.title, post.posted_by.get_full_name()))

    # Test if blog list page loads up, has paginator in place
    def test_if_blog_list_page_loads(self):
        r = self.client.get(reverse('blog:list'))
        self.assertContains(r, 'Epic title 9', 2)
        self.assertContains(r, 'Epic title ', 10)
        self.assertContains(r, 'Older', 1)

        r = self.client.get('%s?page=2' % reverse('blog:list'))
        print(r.content)
        self.assertContains(r, 'Epic title 4', 2)
        self.assertContains(r, 'Newer', 1)

    # Test if blog detail page loads up, has every content
    def test_if_blog_detail_page_loads(self):
        post = Post.objects.latest('pk')
        r = self.client.get(reverse('blog:detail', kwargs={'pk': post.pk}))
        self.assertContains(r, 'Epic title 9', 2)
