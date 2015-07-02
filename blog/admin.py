from django.contrib import admin
from blog.models import Post, Category, Comment


def mark_published(admin, request, queryset):
    queryset.update(active=True)
mark_published.short_description = "Mark stories published"

def mark_unpublished(admin, request, queryset):
    queryset.update(active=False)
mark_unpublished.short_description = "Mark stories unpublished"

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'posted_by', 'posted_on', 'active']
    actions = [mark_published, mark_unpublished]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['pk', 'name']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['posted_by', 'text']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
