from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from home.views import home_page
from home.views import about_page


class HomePageTest(TestCase):
    def test_home_page_uses_home_template(self):
        request = HttpRequest()
        response = home_page(request)
        expected_content = render_to_string('static_pages/home.html')

        self.assertEqual(
            expected_content,
            response.content.decode()
        )

    def test_about_page_uses_about_template(self):
        request = HttpRequest()
        response = about_page(request)
        expected_content = render_to_string('static_pages/about.html')

        self.assertEqual(
            expected_content,
            response.content.decode()
        )
