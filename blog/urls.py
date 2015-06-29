from django.conf.urls import url

from blog.views import Posts, SinglePost

urlpatterns = [
    url(r'posts/', Posts.as_view(), name="list"),
    url(r'post/(?P<pk>\d+)/', SinglePost.as_view(), name="detail")
]
