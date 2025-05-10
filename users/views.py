from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, NewRegistrationForm
from BboardSite.settings import LOGIN_REDIRECT_URL


def register(request):
    # когда отправляем заполненную форму на сервер
    if request.method == 'POST':
        # создаем объект формы с данными из запроса
        form = NewRegistrationForm(request.POST)
        # если форма валидна
        if form.is_valid():
            # создаем объект пользователя без записи в БД
            new_user = form.save(commit=False)
            # хэшируем пароль при помощи set_password
            new_user.set_password(form.cleaned_data['password'])
            # сохраняем пользователя в БД
            new_user.save()
            context = {'title': 'Регистрация завершена', 'new_user': new_user}
            return render(request, template_name='users/registration_done.html', context=context)

    # если метод GET (страница с пустой формой регистрации)
    form = NewRegistrationForm()
    context = {'title': 'Регистрация пользователя', 'register_form': form}
    return render(request, template_name='users/registration.html', context=context)


def log_in(request):
    # создание формы аутенфикации
    form = AuthenticationForm(request, request.POST)
    #проверка формы
    if form.is_valid():
        # полученик логина и пароля из формы
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        # аутентификация пользователя
        # проверка существования пользователя и корректности пароля
        user = authenticate(username=username, password=password)
        if user:
            #авторизация пользователя
            login(request, user)
            # получение дальнейшего маршрута после входа на сайт
            # next - путь, откуда пришел пользователь на страницу входа
            url = request.GET.get('next', LOGIN_REDIRECT_URL)
            return redirect(url)
    context = {'form': form}
    return render(request, template_name='users/login.html', context=context)

def log_out(request):
    logout(request)
    return redirect('bboard:index')

def user_profile(request, pk):
    pass
