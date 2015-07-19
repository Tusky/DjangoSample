from django.conf.urls import url

from user.views import Login, Logout, Register

urlpatterns = [
    url(r'^login/$', Login.as_view(), name="login"),
    url(r'^logout/$', Logout.as_view(), name="logout"),
    url(r'^register/$', Register.as_view(), name="register"),
]
