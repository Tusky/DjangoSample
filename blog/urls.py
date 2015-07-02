from django.conf.urls import url

from blog.views import Posts, SinglePost

urlpatterns = [
    url(r'^search/$', Posts.as_view(), name="search"),
    url(r'^post/(?P<slug>[\w-]+)/$', SinglePost.as_view(), name="detail"),
    url(r'^(?P<type>\w+)/(?P<slug>[\w-]+)/$', Posts.as_view(), name="filter"),
    url(r'$', Posts.as_view(), name="list"),
]
