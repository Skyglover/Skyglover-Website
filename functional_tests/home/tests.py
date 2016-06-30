import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/m/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_projects_page_can_be_accessed_from_home_page(self):
        self.browser.get('http://localhost:8000')
        projects_link = self.browser.find_element_by_id('projects')
        projects_link.click()

        try:
            WebDriverWait(self.browser, 10).until(
                expected_conditions.presence_of_element_located((By.ID, 'title'))
            )
        except TimeoutException:
            self.fail("Page took too much time to load!")

        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual('Projects', h1.text)


if __name__ == "__main__":
    unittest.main(warnings='ignore')
