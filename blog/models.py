from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _


class Post(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    content = models.TextField(_('Content'))
    posted_by = models.ForeignKey(User)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return _('%s by %s') % (self.title, self.posted_by.get_full_name())

    class Meta:
        ordering = ['-posted_on']
