from django.urls import path

from user.views import Login, Logout, Register

app_name = 'user'

urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('register/', Register.as_view(), name="register"),
]
