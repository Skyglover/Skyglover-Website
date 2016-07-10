from django.test import LiveServerTestCase
from selenium import webdriver
from helper.helper import verify_page_h1_is_displayed


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
