from django.shortcuts import render


def index(request):
    """Функция возвращает "главную" страницу"""
    return render(request, 'main/index.html')


def about(request):
    """Функция возвращает "про нас" страницу"""
    return render(request, 'main/about.html')


def test(request):
    """Функция возвращает "контакты" страницу"""
    return render(request, 'main/test.html')


