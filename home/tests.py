from django.test import TestCase
from selenium import webdriver


class HomePageTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/m/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
