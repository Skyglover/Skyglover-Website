from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from projects.views import project_page


class ProjectPageTest(TestCase):
    def test_home_page_uses_home_template(self):
        request = HttpRequest()
        response = project_page(request)
        expected_content = render_to_string('projects/projects.html')

        self.assertEqual(
            expected_content,
            response.content.decode()
        )
