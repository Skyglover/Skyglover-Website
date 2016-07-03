from django.shortcuts import render

from home.models import SomeText


def home_page(request):
    return render(request, 'static_pages/home.html')


def about_page(request):
    about_information = SomeText.objects.get(identifier='about_info').text
    return render(request, 'static_pages/about.html', {
        'about_information': about_information,
    })


def get_in_touch_page(request):

    return render(request, 'static_pages/get_in_touch.html')
