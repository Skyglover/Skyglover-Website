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


class GetInTouchPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/m/chromedriver')
        self.browser.get('http://localhost:8000/get-in-touch/')

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



if __name__ == "__main__":
    unittest.main(warnings='ignore')
