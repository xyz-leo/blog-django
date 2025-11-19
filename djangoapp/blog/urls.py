from django.urls import path
from blog.views import index, post, custom_page, posts_by_author, posts_by_category


app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('post/<slug:slug>/', post, name='post'),
    path('custom-page/<slug:slug>', custom_page, name='custom_page'),
    path('author-posts/<int:author_id>/', posts_by_author, name='posts_by_author'),
    path('category/<slug:slug>/', posts_by_category, name='posts_by_category'),
]
