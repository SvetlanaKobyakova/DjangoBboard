from django.urls import path
from bboard.views import index, about

app_name = 'bboard'
urlpatterns = [
    path('about/', about, name='about'),
    path('', index, name='index'),
]