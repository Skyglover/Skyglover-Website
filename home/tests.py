from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from home.models import SomeText
from home.views import home_page
from home.views import about_page
from home.views import get_in_touch_page


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
        SomeText.objects.create(identifier='about_info', text='Some random text')
        request = HttpRequest()
        response = about_page(request)
        expected_content = render_to_string('static_pages/about.html', {
            'about_information': SomeText.objects.get(identifier='about_info').text,
        })

        self.assertEqual(
            expected_content,
            response.content.decode()
        )

    def test_get_in_touch_page_uses_get_in_touch_template(self):
        request = HttpRequest()
        response = get_in_touch_page(request)
        expected_content = render_to_string('static_pages/get_in_touch.html')

        self.assertEqual(
            expected_content,
            response.content.decode()
        )
