from django.conf.urls import url

from blog.views import Posts, SinglePost, SearchPost, CategoryPostList

urlpatterns = [
    url(r'^search/$', SearchPost.as_view(), name="search"),
    url(r'^categories/(?P<slug>[\w-]+)/$', CategoryPostList.as_view(), name="category"),
    url(r'^post/(?P<slug>[\w-]+)/$', SinglePost.as_view(), name="detail"),
    url(r'$', Posts.as_view(), name="list"),
]
