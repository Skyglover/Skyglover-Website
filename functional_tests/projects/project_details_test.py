from django.test import LiveServerTestCase
from selenium import webdriver

from projects.models import Project


class ProjectDetailsPageTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        Project.objects.create(
            name='project1',
            summary='This is a fucking summary',
            description='This is a really short description.'
        )
        self.project = Project.objects.all()[0]
        self.browser.get(self.live_server_url + '/projects/' + self.project.slug + '/')

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
