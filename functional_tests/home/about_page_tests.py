import os
import unittest

import sys

from django import setup
from selenium import webdriver

sys.path.append("./")
os.environ["DJANGO_SETTINGS_MODULE"] = "SkygloverWebSite.settings"
setup()
from helper.helper import verify_page_h1_is_displayed
from home.models import SomeText


class AboutPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/m/chromedriver')
        self.browser.get('http://localhost:8000/about/')

    def tearDown(self):
        self.browser.quit()

    def test_about_page_elements_are_displayed(self):
        verify_page_h1_is_displayed(self, self.browser, 'About')
        self.verify_about_information_is_displayed()

    def verify_about_information_is_displayed(self):
        about_information = SomeText.objects.all().get(identifier='about_info').text
        about_information_displayed = self.browser.find_element_by_tag_name('p')
        self.assertEqual(about_information, about_information_displayed.text)


if __name__ == "__main__":
    unittest.main(warnings='ignore')
