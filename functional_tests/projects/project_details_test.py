import sys, os, unittest
from django import setup
from selenium import webdriver

sys.path.append("./")
os.environ["DJANGO_SETTINGS_MODULE"] = "SkygloverWebSite.settings"
setup()



class ProjectDetailsPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/m/chromedriver')
        self.browser.get('http://localhost:8000')

    def tearDown(self):
        self.browser.quit()

    def test_projects_are_displayed(self):
        self.fail('Finish test')


if __name__ == "__main__":
    unittest.main(warnings='ignore')
