from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories


def index(request):
    features = [
        {
            "image": "deps/images/index1.jpg",
            "title": "Совершенство механики",
            "description": "Изысканная инженерия внутри каждого корпуса."
        },
        {
            "image": "deps/images/index2.jpg",
            "title": "Мужской стиль",
            "description": "Аксессуар, который подчёркивает мужественность и статус."
        },
        {
            "image": "deps/images/index3.jpg",
            "title": "Символ точности",
            "description": "Часы NoirTime — не просто инструмент, а отражение характера."
        },
        {
            "image": "deps/images/index4.jpg",
            "title": "Технология и эстетика",
            "description": "Слияние современного механизма с безупречным дизайном."
        },
        {
            "image": "deps/images/index5.jpg",
            "title": "Минимализм вне времени",
            "description": "Лёгкость, утонченность и мощь — всё в одном корпусе."
        },
        {
            "image": "deps/images/index6.jpg",
            "title": "Контраст и энергия",
            "description": "Часы, заряженные уверенностью и стилем."
        },
        {
            "image": "deps/images/index7.jpg",
            "title": "Легендарный образ",
            "description": "Для тех, кто выбирает классику с характером."
        },
        {
            "image": "deps/images/index8.jpg",
            "title": "Наследие времени",
            "description": "Сила в деталях. Вечный стиль — сегодня."
        },
    ]
    return render(request, 'main/index.html', {
        'title': 'Noir Time — Главная',
        'content': 'Noir Time — время в лучшем его проявлении',
        'features': features,
    })


def about(request):
    context = {
        'title': 'Noir Time — О нас',
        'content': 'О нас',
        'text_on_page': "Премиальные часы и аксессуары для тех, кто ценит стиль, точность и характер"
    }
    return render(request, 'main/about.html', context)


def contacts(request):
    context = {
        'title': 'Noir Time — Контактная информация',
    }
    return render(request, 'main/contacts.html', context)


def delivery(request):
    context = {
        'title': 'Noir Time — Доставка и оплата',
    }
    return render(request, 'main/delivery.html', context)
