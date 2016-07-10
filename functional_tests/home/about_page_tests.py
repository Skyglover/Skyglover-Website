from django.conf import settings
from django.test import LiveServerTestCase
from selenium import webdriver
from helper.helper import verify_page_h1_is_displayed
from home.models import SomeText


class AboutPageTest(LiveServerTestCase):

    def __init__(self, *args, **kwargs):
        super(LiveServerTestCase, self).__init__(*args, **kwargs)
        if not settings.DEBUG:
            settings.DEBUG = True

    def setUp(self):
        SomeText.objects.create(identifier='about_info', text='We are Skyglover')
        self.browser = webdriver.Chrome()
        self.browser.get('%s%s' % (self.live_server_url, '/about/'))

    def tearDown(self):
        self.browser.quit()

    def test_about_page_elements_are_displayed(self):
        verify_page_h1_is_displayed(self, self.browser, 'About')
        self.verify_about_information_is_displayed()

    def verify_about_information_is_displayed(self):
        about_information = SomeText.objects.all().get(identifier='about_info').text
        about_information_displayed = self.browser.find_element_by_tag_name('p')
        self.assertEqual(about_information, about_information_displayed.text)
