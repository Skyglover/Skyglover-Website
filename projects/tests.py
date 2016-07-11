from django.test import TestCase
from .models import Project


class ProjectPageTest(TestCase):
    def setUp(self):
        Project.objects.create(name='Power Analyzer', slug='power-analyzer',
                               summary='This is a power analyzer system.')

    def tearDown(self):
        Project.objects.all().delete()

    def test_projects_page_uses_projects_template(self):
        response = self.client.get('/projects/')
        self.assertTemplateUsed(response, 'projects/projects.html')

    def test_project_details_page_uses_project_details_template(self):
        response = self.client.get('/projects/' + Project.objects.first().slug + '/')
        self.assertTemplateUsed(response, 'projects/project_details.html')
