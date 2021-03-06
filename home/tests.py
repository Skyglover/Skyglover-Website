from django.core.urlresolvers import resolve
from django.test import TestCase

from helper.helper import assert_path_uses_template
from home.models import SomeText
from home.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_uses_home_template(self):
        assert_path_uses_template(self, '/', 'static_pages/home.html')

    def test_about_page_uses_about_template(self):
        SomeText.objects.create(identifier='about_info', text='Some random text')
        assert_path_uses_template(self, '/about/', 'static_pages/about.html')

    def test_get_in_touch_page_uses_get_in_touch_template(self):
        assert_path_uses_template(self, '/get-in-touch/', 'static_pages/get_in_touch.html')
