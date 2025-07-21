from django.urls import path
from bboard.views import (index, about, add_post,
                          read_post, update_post, delete_post,
                          user_posts, user_info, search_post,
                          filter_post, upload_photos, add_to_favorites,
                          remove_from_favorites, favorites_list)

app_name = 'bboard'
urlpatterns = [
    path('search/', search_post, name='search_post'),
    path('filter/', filter_post, name='filter_post'),
    path('about/', about, name='about'),
    path('post/<slug:slug>/add_favorite/', add_to_favorites, name='add_to_favorites'),
    path('post/<slug:slug>/remove_favorite/', remove_from_favorites, name='remove_from_favorites'),
    path('favorites/', favorites_list, name='favorites_list'),
    path('post/<int:pk>/delete/', delete_post, name='delete_post'),
    path('post/user/info/<int:user_id>/', user_info, name='user_info'),
    path('post/user/<int:user_id>/', user_posts, name='user_posts'),
    path('post/<int:pk>/edit/', update_post, name='update_post'),
    path('post/<slug:slug>/', read_post, name='read_post'),
    path('post/', add_post, name='add_post'),
    path('', index, name='index'),
    path('upload/', upload_photos, name='upload_photos'),
]
