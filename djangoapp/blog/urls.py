from django.urls import path
from blog.views import BaseListView, post, custom_page, PostsByAuthorListView, PostsByCategoryListView, PostsByTagListView, PostSearchListView


app_name = 'blog'

urlpatterns = [
    path('', BaseListView.as_view(), name='index'),
    path('post/<slug:slug>/', post, name='post'),
    path('page/<slug:slug>', custom_page, name='custom_page'),

    path('author-posts/<int:author_id>/', PostsByAuthorListView.as_view(), name='posts_by_author'),
    path('category/<slug:slug>/', PostsByCategoryListView.as_view(), name='posts_by_category'),
    path('tag/<slug:slug>/', PostsByTagListView.as_view(), name='posts_by_tag'),
    path('search/', PostSearchListView.as_view(), name='search'),
]
