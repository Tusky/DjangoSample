from django.contrib import admin
from blog.models import Post, Category

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

    # Override GET to preselect current user in admin.
    def add_view(self, request, form_url='', extra_context=None):
        g = request.GET.copy()
        g.update({'posted_by': request.user.pk,})
        request.GET = g
        return super(PostAdmin, self).add_view(request, form_url, extra_context)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['pk', 'name']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
