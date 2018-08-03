from django import forms
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import modelform_factory
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, RedirectView, CreateView


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
    success_url = reverse_lazy('user:login')
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
