from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'posted_by', 'posted_on']

admin.site.register(Post)
