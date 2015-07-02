from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from blog.models import Post, Category

class BlogTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.blogger = User.objects.create_superuser(username='blogger', password='blogger', email='a@a.com')
        self.client.login(username='blogger', password='blogger')
        self.category = Category.objects.create(name='Category', slug='category')
        for i in range(10):
            Post.objects.create(
                title='Epic title %d' % i,
                slug='epic-title-%d' % i,
                content='This is the content for Epic title %d' % i,
                posted_by=self.blogger,
                active=True
            )

    # Test if model's __str__ returns the correct details.
    def test_model_str(self):
        post = Post.objects.latest('pk')
        self.assertEqual(post.__str__(), "%s by %s" % (post.title, post.posted_by.get_full_name()))

        self.assertEqual(self.category.__str__(), 'Category')

    # Test if blog list page loads up, has paginator in place
    def test_if_blog_list_page_loads(self):
        r = self.client.get(reverse('blog:list'))
        self.assertContains(r, 'Epic title 9', 2)
        self.assertContains(r, 'Epic title ', 10)
        self.assertContains(r, 'Older', 1)

        r = self.client.get('%s?page=2' % reverse('blog:list'))
        self.assertContains(r, 'Epic title 4', 2)
        self.assertContains(r, 'Newer', 1)

    # Test if blog detail page loads up, has every content
    def test_if_blog_detail_page_loads(self):
        post = Post.objects.latest('pk')
        r = self.client.get(reverse('blog:detail', kwargs={'slug': post.slug}))
        self.assertContains(r, 'Epic title 9', 2)

    # Test if search page loads up, has every content
    def test_if_search_page_loads(self):
        r = self.client.get('%s?q=Epic Title 9' % reverse('blog:search'))
        self.assertContains(r, 'Epic title 9', 2)

    # Test if category filter page loads up, has every content
    def test_if_category_page_loads(self):
        post = Post.objects.latest('pk')
        post.categories.add(self.category)
        r = self.client.get(reverse('blog:filter', kwargs={'type': 'category', 'slug': self.category.slug}))
        self.assertContains(r, 'Epic title 9', 2)

    # Test if user filter page loads up, has every content
    def test_if_user_filter_page_loads(self):
        new_blogger = User.objects.create(username='teszt_elek', password='teszt_elek')
        post = Post.objects.latest('pk')
        post.posted_by=new_blogger
        post.save()
        r = self.client.get(reverse('blog:filter', kwargs={'type': 'user', 'slug': new_blogger.username}))
        self.assertContains(r, post.title, 2)

    def test_admin_features(self):
        data = {
            'action': 'mark_unpublished',
            '_selected_action': [post.pk for post in Post.objects.all()]
        }
        self.client.post(reverse('admin:blog_post_changelist'), data=data)
        self.assertEqual(Post.objects.filter(active=True).count(), 0)
        self.assertEqual(Post.objects.filter(active=False).count(), 10)

        data = {
            'action': 'mark_published',
            '_selected_action': [post.pk for post in Post.objects.all()]
        }
        self.client.post(reverse('admin:blog_post_changelist'), data=data)
        self.assertEqual(Post.objects.filter(active=False).count(), 0)
        self.assertEqual(Post.objects.filter(active=True).count(), 10)


