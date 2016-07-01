import sys, os, unittest
from django import setup
from selenium import webdriver

sys.path.append("./")
os.environ["DJANGO_SETTINGS_MODULE"] = "SkygloverWebSite.settings"
setup()
from projects.models import Project


class ProjectDetailsPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/m/chromedriver')
        self.project = Project.objects.all()[0]
        self.browser.get('http://localhost:8000/projects/' + self.project.slug + '/')

    def tearDown(self):
        self.browser.quit()

    def test_project_details_are_displayed(self):
        self.verify_project_name()
        self.verify_status()
        self.verify_start_date()
        self.verify_description()

    def verify_description(self):
        description = self.browser.find_element_by_id('description')
        self.assertEqual(self.project.description, description.text)

    def verify_start_date(self):
        self.assertEqual('Start date: ' + self.project.get_start_date(),
                         self.browser.find_element_by_id('start_date').text)

    def verify_status(self):
        self.assertEqual('Status: ' + self.project.status,
                         self.browser.find_element_by_id('status').text)

    def verify_project_name(self):
        self.assertEqual(self.project.name, self.browser.find_element_by_id('name').text)


if __name__ == "__main__":
    unittest.main(warnings='ignore')
