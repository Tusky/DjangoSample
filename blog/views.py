from django.db.models import Q

from django.views.generic import ListView, DetailView

from blog.models import Post, Category


class Posts(ListView):
    """
    Display every post paginated.
    """
    model = Post
    template_name = 'posts.html'
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.for_display()


class SinglePost(DetailView):
    """
    Display a single selected post.
    """
    model = Post
    template_name = 'post.html'

    def get_queryset(self):
        return self.model.objects.for_display()


class SearchPost(ListView):
    """
    List posts that are matching queries according to the search.
    """
    model = Post
    template_name = 'posts.html'
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.for_display().filter(
            Q(title__icontains=self.request.GET.get('q', '')) | Q(content__icontains=self.request.GET.get('q', '')))


class CategoryPostList(ListView):
    """
    List posts that are part of a given category.
    """
    model = Post
    template_name = 'posts.html'
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.for_display().filter(categories__slug=self.kwargs.get('slug', ''))
