from django.urls import path

from blog.views import Posts, SinglePost, PostComment

app_name = 'blog'

urlpatterns = [
    path('search/', Posts.as_view(), name="search"),
    path('post/<str:slug>/add_comment/', PostComment.as_view(), name="add-comment"),
    path('post/<str:slug>/', SinglePost.as_view(), name="detail"),
    path('<str:type>/<str:slug>/', Posts.as_view(), name="filter"),
    path('', Posts.as_view(), name="list"),
]
