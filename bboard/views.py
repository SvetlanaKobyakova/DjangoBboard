from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post
from .forms import PostForm, FilterForm
from .forms import MultiplePhotoForm
from .models import Photo


def index(request):
    # получение всех постов, отсортированных по дате публикации
    # (select * from bboard_post order by created_at DESK)
    posts = Post.objects.all().order_by('-created_at')
    count_posts = Post.objects.count()
    # показываем по три поста на странице
    per_page = 4
    paginator = Paginator(posts, per_page)
    # получаем номер страницы из URL
    page_number = request.GET.get('page')
    # получаем объекты для текущей страницы
    page_obj = paginator.get_page(page_number)
    filter_form = FilterForm
    context = {
        'title':'Главная страница',
        'page_obj': page_obj,
        'count_posts': count_posts,
        'filter_form': filter_form
    }
    return render(request, template_name='bboard/index.html', context=context)


def about(request):
    count_posts = Post.objects.count()
    context = {'title': 'О сайте', 'count_posts': count_posts}
    return render(request, template_name='bboard/about.html', context=context)

@login_required
def add_post(request):
    if request.method == 'GET':
        post_form = PostForm(author=request.user)
        context = {'title': 'Добавить объявление','form': post_form}
        return render(request, template_name='bboard/post_add.html', context=context)

    if request.method == 'POST':
        post_form = PostForm(data=request.POST, files=request.FILES, author=request.user)
        if post_form.is_valid():
            # post = Post()
            # post.title = post_form.cleaned_data['title']
            # post.rooms = post_form.cleaned_data['rooms']
            # post.square = post_form.cleaned_data['square']
            # post.floor = post_form.cleaned_data['floor']
            # post.price = post_form.cleaned_data['price']
            # post.metro = post_form.cleaned_data['metro']
            # post.city = post_form.cleaned_data['city']
            # post.street = post_form.cleaned_data['street']
            # post.house = post_form.cleaned_data['house']
            # post.apartment = post_form.cleaned_data['apartment']
            # post.text = post_form.cleaned_data['text']
            # post.author = post_form.cleaned_data['author']
            # post.image = post_form.cleaned_data['image']
            # post.save()
            post_form.save()
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
        post_form = PostForm(data=request.POST,
                             files=request.FILES,
                             instance=post,
                             initial={'author':post.author})
        if post_form.is_valid():
            post_form.save()
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

def user_posts(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # posts = user.posts.all()
    posts = Post.objects.filter(author=user).select_related('author')
    context = {'user': user, 'posts': posts}
    return render(request, template_name='bboard/user_posts.html', context=context)


@login_required
def user_info(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {'user': user}
    return render(request, template_name='bboard/user_info.html', context=context)

def page_not_found(request, exception):
    return render(request, template_name='bboard/404.html', context={'title': '404'})


def forbidden(request, exception):
    return render(request, template_name='bboard/403.html', context={'title': '403'})


def server_error(request):
    return render(request, template_name='bboard/500.html', context={'title': '500'})


def search_post(request):
    query = request.GET.get('query')
    query_text = Q(title__icontains=query) | Q(metro__icontains=query) | Q(street__icontains=query)
    results = Post.objects.filter(query_text)

    per_page = 4
    paginator = Paginator(results, per_page)
    # получаем номер страницы из URL
    page_number = request.GET.get('page')
    # получаем объекты для текущей страницы
    page_obj = paginator.get_page(page_number)
    count_posts = results.count()
    context = {
        'title': 'Главная страница',
        'page_obj': page_obj,
        'count_posts': count_posts
    }
    return render(request, template_name='bboard/index.html', context=context)

def filter_post(request):
    author_id = request.GET.get('author')
    if not author_id:
        results = Post.objects.all()
    else:
        author = User.objects.get(pk=author_id)
        query_text = Q(author__exact=author)
        results = Post.objects.filter(query_text)

    per_page = 4
    paginator = Paginator(results, per_page)
    # получаем номер страницы из URL
    page_number = request.GET.get('page')
    # получаем объекты для текущей страницы
    page_obj = paginator.get_page(page_number)
    count_posts = results.count()
    filter_form = FilterForm
    context = {
        'title': 'Главная страница',
        'page_obj': page_obj,
        'count_posts': count_posts,
        'filter_form': filter_form
    }
    return render(request, template_name='bboard/index.html', context=context)

 # новое представление для загрузки несколько фото
def upload_photos(request):
    if request.method == 'POST':
        form = MultiplePhotoForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('image')  # Получаем список файлов
            for file in files:
                Photo.objects.create(images=file)  # Создаем запись для каждого файла
            return redirect('bboard/index.html')  # Замените на ваш URL
    else:
        form = MultiplePhotoForm()

        # MAX_FILES = 5
        # if len('files') > MAX_FILES:
        #     form.add_error('image', f'Максимум {MAX_FILES} файлов.')

    return render(request, 'bboard/upload.html', {'form': form})