from django.conf.urls import url

from blog.views import Posts, SinglePost, PostComment, Login

urlpatterns = [
    url(r'^search/$', Posts.as_view(), name="search"),
    url(r'^login/$', Login.as_view(), name="login"),
    url(r'^post/(?P<slug>[\w-]+)/add_comment/$', PostComment.as_view(), name="add-comment"),
    url(r'^post/(?P<slug>[\w-]+)/$', SinglePost.as_view(), name="detail"),
    url(r'^(?P<type>\w+)/(?P<slug>[\w-]+)/$', Posts.as_view(), name="filter"),
    url(r'$', Posts.as_view(), name="list"),
]
