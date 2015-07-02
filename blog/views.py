from django.db.models import Q
from django.views.generic import ListView, DetailView

from blog.models import Post


class Posts(ListView):
    """
    Display every post paginated or if given a type filter/search for it.
    """
    model = Post
    template_name = 'posts.html'
    paginate_by = 5

    def get_queryset(self):
        qs = self.model.objects.for_display()
        type_of_page = self.kwargs.get('type', False)
        search_query = self.request.GET.get('q', False)
        if type_of_page == 'user':
            qs = qs.filter(posted_by__username=self.kwargs.get('slug', ''))
        elif type_of_page == 'category':
            qs = qs.filter(categories__slug=self.kwargs.get('slug', ''))
        if search_query:
            qs = qs.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
        return qs


class SinglePost(DetailView):
    """
    Display a single selected post.
    """
    model = Post
    template_name = 'post.html'

    def get_queryset(self):
        return self.model.objects.for_display()
