from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse

menu = [
    {'title': "О магазине", 'url_name': 'about'},
    {'title': "Добавить товар", 'url_name': 'add_page'},
    {'title': "Контакты", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]

# База данных товаров
data_db = [
    {
        'id': 1,
        'title': 'Цемент М500',
        'content': '''<h1>Цемент М500</h1> Универсальный портландцемент с высокой прочностью. Подходит для бетона, стяжек и кладки. Упаковка 50 кг.''',
        'is_published': True
    },
    {
        'id': 2,
        'title': 'Эмаль ПФ-115',
        'content': 'Классическая масляная краска для наружных и внутренних работ. Белая, банка 2.7 л.',
        'is_published': True
    },
    {
        'id': 3,
        'title': 'Шпаклёвка финишная',
        'content': 'Финишная шпаклёвка для идеально гладкой поверхности. Подходит под покраску и обои.',
        'is_published': False
    },
]

# Категории товаров
cats_db = [
    {'id': 1, 'name': 'Сухие смеси'},
    {'id': 2, 'name': 'Краски'},
    {'id': 3, 'name': 'Инструменты'},
]

def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,
    }
    return render(request, 'shop/index.html', context=data)

def about(request):
    return render(request, 'shop/about.html', {'title': 'О магазине', 'menu': menu})

def show_post(request, post_id):
    # Заглушка (можно переделать позже на поиск по ID и отрисовку карточки)
    return HttpResponse(f"Информация о товаре с id = {post_id}")

def addpage(request):
    return HttpResponse("Добавление нового товара")

def contact(request):
    return HttpResponse("Контактная информация")

def login(request):
    return HttpResponse("Страница авторизации")

def show_category(request, cat_id):
    data = {
        'title': 'Товары по категориям',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'shop/index.html', context=data)

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
