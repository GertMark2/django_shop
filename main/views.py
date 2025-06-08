from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин  HOME',
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': "Текст о том,почему это магазин такой прекрасный и насколько качественный товар"
    }
    return render(request, 'main/about.html', context)
