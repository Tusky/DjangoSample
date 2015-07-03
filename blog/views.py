from django import forms

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
from django.forms import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, FormView, RedirectView

from blog.models import Post, Comment


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


class PostComment(CreateView):
    """
    Saves comments received to a post. Removed ability to GET the page.
    """
    model = Comment
    fields = ['text']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PostComment, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('blog:detail', kwargs={'slug': self.kwargs['slug']}))

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.posted_by = self.request.user
        comment.post = get_object_or_404(Post, slug=self.kwargs['slug'])
        comment.save()
        messages.success(self.request, 'Your comment was posted.')
        return super(PostComment, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'slug': self.kwargs['slug']})


class Login(FormView):
    """
    Logs in the user then redirects him back to home or back to the page he came from.
    """
    form_class = AuthenticationForm
    template_name = 'login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

    def get_success_url(self):
        next_url = self.request.GET.get('next', False)
        redirect_to = reverse('blog:list') if not next_url else next_url
        return redirect_to

    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context['current_page'] = 'login'
        return context


class Logout(RedirectView):
    """
    Logs out the currently logged in user.
    """
    permanent = False
    url = reverse_lazy('blog:list')

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super(Logout, self).dispatch(request, *args, **kwargs)


class Register(CreateView):
    """
    Page for handling user sign ups.
    """
    model = User
    fields = ['username', 'password', 'first_name', 'last_name']
    success_url = reverse_lazy('blog:login')
    template_name = 'register.html'
    widgets = {
        'password': forms.PasswordInput
    }

    def get_form_class(self):
        return modelform_factory(self.model, fields=self.fields, widgets=self.widgets)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        return super(Register, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Register, self).get_context_data(**kwargs)
        context['current_page'] = 'register'
        return context
