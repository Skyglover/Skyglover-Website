from django.shortcuts import render


def home_page(request):
    return render(request, 'static_pages/home.html')


def about_page(request):
    return render(request, 'static_pages/about.html')


def get_in_touch_page(request):
    return render(request, 'static_pages/get_in_touch.html')