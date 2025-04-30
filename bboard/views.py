from django.shortcuts import render
from django.template.context_processors import request

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
    if request.method == 'GET':
        post_form = PostForm()
        context = {'title': 'Добавить объявление','form': post_form}
        return render(request, template_name='bboard/post_add.html', context=context)

    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post = Post()
            post.title = post_form.cleaned_data['title']
            post.rooms = post_form.cleaned_data['rooms']
            post.square = post_form.cleaned_data['square']
            post.floor = post_form.cleaned_data['floor']
            post.price = post_form.cleaned_data['price']
            post.metro = post_form.cleaned_data['metro']
            post.city = post_form.cleaned_data['city']
            post.street = post_form.cleaned_data['street']
            post.house = post_form.cleaned_data['house']
            post.apartment = post_form.cleaned_data['apartment']
            post.text = post_form.cleaned_data['text']
            post.author = post_form.cleaned_data['author']
            post.save()
            return index(request)
        return None
    return None

def read_post(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'title': 'Информация об объекте', 'post': post}
    return render(request, template_name='bboard/post_detail.html', context=context)

