from django.shortcuts import render_to_response


def home_page(request):
    return render_to_response('static_pages/home.html')
