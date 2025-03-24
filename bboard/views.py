from django.shortcuts import render


def index(request):
    context = {"title":"Главная страница"}
    return render(request, template_name='bboard/index.html', context=context)

def about(request):
    context = {"title": "О сайте"}
    return render(request, template_name='bboard/about.html', context=context)
