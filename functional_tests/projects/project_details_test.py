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
        #TODO: title, status, start_date, long_description are displayed
        self.fail('Finish test')


if __name__ == "__main__":
    unittest.main(warnings='ignore')
