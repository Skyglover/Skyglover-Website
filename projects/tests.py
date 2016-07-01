from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from projects.views import projects_page
from projects.views import project_details_page
from .models import Project


class ProjectPageTest(TestCase):
    def setUp(self):
        Project.objects.create(name='Power Analyzer', slug='power-analyzer',
                               summary='This is a power analyzer system.')

    def tearDown(self):
        Project.objects.all().delete()

    def test_projects_page_uses_projects_template(self):
        request = HttpRequest()
        response = projects_page(request)
        expected_content = render_to_string('projects/projects.html', {
            'projects': Project.objects.all(),
        })

        self.assertEqual(
            expected_content,
            response.content.decode()
        )

    def test_project_details_page_uses_project_details_template(self):
        project = Project.objects.all()[0]
        request = HttpRequest()
        response = project_details_page(request, project.slug)
        expected_content = render_to_string('projects/project_details.html', {
            'project': project,
        })

        self.assertEqual(
            expected_content,
            response.content.decode()
        )
