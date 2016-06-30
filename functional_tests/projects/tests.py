import os
import sys
import unittest
from django import setup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

sys.path.append("./")
sys.path.append("./functional_tests/util/")

os.environ["DJANGO_SETTINGS_MODULE"] = "SkygloverWebSite.settings"
setup()
from projects.models import Project
# noinspection PyUnresolvedReferences
from util import wait_for_page_to_load_with_id


class ProjectsPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/m/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_projects_are_displayed(self):
        self.browser.get('http://localhost:8000')
        projects_link = self.browser.find_element_by_id('projects')
        projects_link.click()

        try:
            wait_for_page_to_load_with_id(self.browser, 'title')
        except TimeoutException:
            self.fail("Page took too much time to load!")

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


if __name__ == "__main__":
    unittest.main(warnings='ignore')
