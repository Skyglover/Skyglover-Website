import sys, os, unittest
from django import setup
from selenium import webdriver

sys.path.append("./")
os.environ["DJANGO_SETTINGS_MODULE"] = "SkygloverWebSite.settings"
setup()
from projects.models import Project
from helper.helper import wait_for_page_to_load_with_id_or_fail
from helper.helper import verify_page_h1_is_displayed


class ProjectsPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/m/chromedriver')
        self.browser.get('http://localhost:8000')

    def tearDown(self):
        self.browser.quit()

    def test_projects_are_displayed(self):
        self.navigate_to_projects()
        verify_page_h1_is_displayed(self, self.browser, 'Projects')
        self.verify_projects_are_displayed()

    def test_label_is_displayed_when_no_projects_available(self):
        projects = Project.objects.all()
        projects_copy = list(projects)
        projects.delete()

        self.navigate_to_projects()
        label = self.browser.find_element_by_id('no_projects_label')
        self.assertEquals('Currently there are no projects to show.', label.text)

        for project in projects_copy:
            project.save()

    def verify_projects_are_displayed(self):
        projects = Project.objects.all()
        displayed_projects = self.browser.find_elements_by_class_name('project')

        self.assertEqual(len(projects), len(displayed_projects))

        for index in range(len(projects)):
            project_name = displayed_projects[index].find_element_by_tag_name('li').text
            project_description = displayed_projects[index].find_element_by_tag_name('p').text
            self.assertEqual(projects[index].name, project_name)
            self.assertEqual(projects[index].description, project_description)

    def navigate_to_projects(self):
        projects_link = self.browser.find_element_by_id('projects')
        projects_link.click()
        wait_for_page_to_load_with_id_or_fail(self, self.browser, 'projects_page_title')


if __name__ == "__main__":
    unittest.main(warnings='ignore')
