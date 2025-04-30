from django.urls import path
from bboard.views import index, about, add_post, read_post

app_name = 'bboard'
urlpatterns = [
    path('about/', about, name='about'),
    path('post/<int:pk>/', read_post, name='read_post'),
    path('post/', add_post, name='add_post'),
    path('', index, name='index'),
]

