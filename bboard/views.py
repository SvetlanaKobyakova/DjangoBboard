from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm


def index(request):
    # получение всех постов, отсортированных по дате публикации
    # (select * from bboard_post order by created_at DESK)
    posts = Post.objects.all().order_by('-created_at')
    # показываем по три поста на странице
    per_page = 4
    paginator = Paginator(posts, per_page)
    # получаем номер страницы из URL
    page_number = request.GET.get('page')
    # получаем объекты для текущей страницы
    page_obj = paginator.get_page(page_number)
    context = {'title':'Главная страница', 'page_obj': page_obj}
    return render(request, template_name='bboard/index.html', context=context)


def about(request):
    context = {'title': 'О сайте'}
    return render(request, template_name='bboard/about.html', context=context)

@login_required
def add_post(request):
    if request.method == 'GET':
        post_form = PostForm()
        context = {'title': 'Добавить объявление','form': post_form}
        return render(request, template_name='bboard/post_add.html', context=context)

    if request.method == 'POST':
        post_form = PostForm(data=request.POST, files=request.FILES)
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
            post.image = post_form.cleaned_data['image']
            post.save()
            return index(request)
        return None
    return None


def read_post(request, slug):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, slug=slug)
    context = {'title': 'Информация об объекте', 'post': post}
    return render(request, template_name='bboard/post_detail.html', context=context)

@login_required
def update_post(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post_form = PostForm(data=request.POST, files=request.FILES)
        if post_form.is_valid():
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
            post.image = post_form.cleaned_data['image']
            post.save()
            return redirect('bboard:read_post', slug=post.slug)
        return None
    else:
        post_form = PostForm(initial={
            'title': post.title,
            'rooms': post.rooms,
            'square': post.square,
            'floor': post.floor,
            'price': post.price,
            'metro': post.metro,
            'city': post.city,
            'street': post.street,
            'house': post.house,
            'apartment': post.apartment,
            'text': post.text,
            'author': post.author,
            'image': post.image,
        })
        return render(request, template_name='bboard/post_edit.html', context={'form': post_form})


def delete_post(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    if request.method == 'POST':
        post.delete()
        return redirect('bboard:index')
    return render(request, template_name='bboard/post_delete.html', context=context)


def page_not_found(request, exception):
    return render(request, template_name='bboard/404.html', context={'title': '404'})


def forbidden(request, exception):
    return render(request, template_name='bboard/403.html', context={'title': '403'})


def server_error(request):
    return render(request, template_name='bboard/500.html', context={'title': '500'})

