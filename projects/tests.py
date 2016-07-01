from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from projects.views import projects_page


class ProjectPageTest(TestCase):
    def test_projects_page_uses_projects_template(self):
        request = HttpRequest()
        response = projects_page(request)
        expected_content = render_to_string('projects/projects.html')

        self.assertEqual(
            expected_content,
            response.content.decode()
        )
