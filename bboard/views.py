from django.shortcuts import render
from .models import Post
from .forms import PostForm


def index(request):
    # получение всех постов (select * from bboard_post)
    posts = Post.objects.all()
    context = {'title':'Главная страница', 'posts': posts}
    return render(request, template_name='bboard/index.html', context=context)

def about(request):
    context = {'title': 'О сайте'}
    return render(request, template_name='bboard/about.html', context=context)

def add_post(request):
    post_form = PostForm()
    context = {'form': post_form}
    return render(request, template_name='bboard/post_add.html', context=context)