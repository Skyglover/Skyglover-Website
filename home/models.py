import unittest

import sys
from selenium import webdriver

sys.path.append("./")
from helper.helper import verify_page_h1_is_displayed


class AboutPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/m/chromedriver')
        self.browser.get('http://localhost:8000/about/')

    def tearDown(self):
        self.browser.quit()

    def test_about_page_elements_are_displayed(self):
        verify_page_h1_is_displayed(self, self.browser, 'About')
        about_information = self.browser.find_element_by_tag_name('p')
        self.assertEqual('We are ...', about_information.text)

if __name__ == "__main__":
    unittest.main(warnings='ignore')
