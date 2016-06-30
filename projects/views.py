from django.shortcuts import render
from .models import Project


def projects_page(request):
    return render(request, 'projects/projects.html', {
        'projects': Project.objects.all(),
    })
