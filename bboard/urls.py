from django.urls import path
from bboard.views import (index, about, add_post,
                          read_post, update_post, delete_post)

app_name = 'bboard'
urlpatterns = [
    path('about/', about, name='about'),
    path('post/<int:pk>/delete/', delete_post, name='delete_post'),
    path('post/<int:pk>/edit/', update_post, name='update_post'),
    path('post/<slug:slug>/', read_post, name='read_post'),
    path('post/', add_post, name='add_post'),
    path('', index, name='index'),
]

