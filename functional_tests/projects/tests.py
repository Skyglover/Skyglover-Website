import sys, os, unittest
from django import setup
from selenium import webdriver

sys.path.append("./")
os.environ["DJANGO_SETTINGS_MODULE"] = "SkygloverWebSite.settings"
setup()
from projects.models import Project
from helper.helper import wait_for_page_to_load_with_id_or_fail


class ProjectsPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/m/chromedriver')
        self.browser.get('http://localhost:8000')
        projects_link = self.browser.find_element_by_id('projects')
        projects_link.click()
        wait_for_page_to_load_with_id_or_fail(self, self.browser, 'title')

    def tearDown(self):
        self.browser.quit()

    def test_projects_are_displayed(self):
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

    def test_label_is_displayed_when_no_projects_available(self):
        # TODO: navigate to projects
        # TODO: I see a label that indicates that currently there are no projects
        self.fail("Complete tests")

if __name__ == "__main__":
    unittest.main(warnings='ignore')
