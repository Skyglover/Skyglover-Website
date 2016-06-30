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


class ProjectsPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/m/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_projects_are_displayed(self):
        self.browser.get('http://localhost:8000')
        projects_link = self.browser.find_element_by_id('projects')
        projects_link.click()

        self.wait_for_page_to_load_with_id('title')

        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual('Projects', h1.text)

        projects = Project.objects.all()
        displayed_projects = self.browser.find_elements_by_class_name('project')

        self.assertEqual(len(projects), len(displayed_projects))

        for index in range(len(projects)):
            project_name = displayed_projects[index].find_element_by_tag_name('li').text
            project_description = displayed_projects[index].find_element_by_tag_name('p').text
            self.assertEqual(projects[index].name, project_name)
            self.assertEqual(projects[index].description, project_description)

    def wait_for_page_to_load_with_id(self, page_id, time_to_wait=10):
        try:
            WebDriverWait(self.browser, time_to_wait).until(
                expected_conditions.presence_of_element_located((By.ID, page_id))
            )
        except TimeoutException:
            self.fail("Page took too much time to load!")


if __name__ == "__main__":
    unittest.main(warnings='ignore')
