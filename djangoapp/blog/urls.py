from django.urls import path
from blog.views import index, post, custom_page


app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('post/<slug:slug>/', post, name='post'),
    path('custom-page', custom_page, name='custom_page')
]
