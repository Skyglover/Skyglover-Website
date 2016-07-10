from django.test import LiveServerTestCase
from selenium import webdriver
from helper.helper import verify_page_h1_is_displayed
from home.models import SomeText


class AboutPageTest(LiveServerTestCase):
    def setUp(self):
        SomeText.objects.create(identifier='about_info', text='We are Skyglover')
        self.browser = webdriver.Chrome()
        self.browser.get(self.live_server_url + '/about/')

    def tearDown(self):
        self.browser.quit()

    def test_about_page_elements_are_displayed(self):
        verify_page_h1_is_displayed(self, self.browser, 'About')
        self.verify_about_information_is_displayed()

    def verify_about_information_is_displayed(self):
        about_information = SomeText.objects.all().get(identifier='about_info').text
        about_information_displayed = self.browser.find_element_by_tag_name('p')
        self.assertEqual(about_information, about_information_displayed.text)


class GetInTouchPageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get(self.live_server_url + '/get-in-touch/')

    def tearDown(self):
        self.browser.quit()

    def test_get_in_touch_page_elements_are_displayed(self):
        verify_page_h1_is_displayed(self, self.browser, 'Get In Touch')
        twitter = self.browser.find_element_by_id('twitter').text
        github = self.browser.find_element_by_id('github').text
        email = self.browser.find_element_by_id('email').text
        address = self.browser.find_element_by_tag_name('footer').text
        self.assertEqual('Twitter', twitter)
        self.assertEqual('Github', github)
        self.assertEqual('Email', email)
        self.assertEqual('Quito, Ecuador', address)
