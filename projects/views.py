from django.shortcuts import render, get_object_or_404
from .models import Project


def projects_page(request):
    return render(request, 'projects/projects.html', {
        'projects': Project.objects.all(),
    })


def project_details_page(request, project_name_slug):
    project = get_object_or_404(Project, slug=project_name_slug)
    return render(request, 'projects/project_details.html', {
        'project': project,
    })
