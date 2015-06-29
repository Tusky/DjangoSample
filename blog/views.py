from django.views.generic import ListView, DetailView

from blog.models import Post


class Posts(ListView):
    model = Post
    template_name = 'posts.html'
    paginate_by = 5

class SinglePost(DetailView):
    model = Post
    template_name = 'post.html'
