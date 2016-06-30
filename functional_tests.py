import os
import sys
import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from django import setup

sys.path.append("./")
os.environ["DJANGO_SETTINGS_MODULE"] = "SkygloverWebSite.settings"
setup()
from projects.models import Project


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

        project_names = ['Power Analyzer', 'Skyglover Website']
        project_descriptions = ['This is a power analyzer system.', 'This is a website for Skyglover.']

        projects = self.browser.find_elements_by_class_name('project')

        self.assertEqual(2, len(projects))

        for index in range(len(projects)):
            project_name = projects[index].find_element_by_tag_name('li').text
            project_description = projects[index].find_element_by_tag_name('p').text
            self.assertEqual(project_names[index], project_name)
            self.assertEqual(project_descriptions[index], project_description)


if __name__ == "__main__":
    unittest.main(warnings='ignore')
