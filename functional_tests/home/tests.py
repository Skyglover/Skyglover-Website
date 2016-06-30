import unittest
import sys
from selenium import webdriver
sys.path.append("./")
from helper.helper import wait_for_page_to_load_with_id_or_fail


class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/m/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_projects_page_can_be_accessed_from_home_page(self):
        self.browser.get('http://localhost:8000')
        projects_link = self.browser.find_element_by_id('projects')
        projects_link.click()

        wait_for_page_to_load_with_id_or_fail(self, self.browser, 'title')
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual('Projects', h1.text)


if __name__ == "__main__":
    unittest.main(warnings='ignore')
