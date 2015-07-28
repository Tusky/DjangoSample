from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _


class Category(models.Model):
    name = models.CharField(_('Category'), max_length=255)
    slug = models.SlugField(_('Slug'))

    def __str__(self):
        return self.name


class PostManager(models.Manager):
    """
    Only display Active posts instead everything.
    """

    def for_display(self):
        return super(PostManager, self).get_queryset().filter(active=True)


class Post(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(_('Slug'))
    content = models.TextField(_('Content'))
    posted_by = models.ForeignKey(User, verbose_name=_('Posted by'))
    posted_on = models.DateTimeField(auto_now_add=True, verbose_name=_('Posted on'))
    categories = models.ManyToManyField(Category, verbose_name=_('Categories'), blank=True)
    active = models.BooleanField(_('Active'), default=False)
    objects = PostManager()

    def __str__(self):
        return _('%s by %s') % (self.title, self.posted_by.get_full_name())

    class Meta:
        ordering = ['-posted_on', '-pk']


class Comment(models.Model):
    text = models.TextField(_('Comment'))
    posted_by = models.ForeignKey(User, verbose_name=_('Posted by'))
    posted_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, verbose_name='Post', related_name='comments')

    class Meta:
        ordering = ['-posted_on']
