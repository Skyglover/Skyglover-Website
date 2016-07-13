from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from helper.helper import verify_page_h1_is_displayed
from helper.helper import wait_for_page_to_load_with_id_or_fail
from projects.models import Project


class ProjectsPageTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def go_to_projects(self):
        self.browser.get(self.live_server_url + '/projects/')

    def tearDown(self):
        self.browser.quit()

    def test_projects_are_displayed(self):
        Project.objects.create(name='project1', summary='This is a fucking summary')
        Project.objects.create(name='project2', summary='This is a fucking summary')
        self.go_to_projects()
        self.verify_projects_title_is_displayed()
        self.verify_projects_are_displayed()
        Project.objects.all().delete()

    def test_label_is_displayed_when_no_projects_available(self):
        self.go_to_projects()
        self.verify_projects_title_is_displayed()

        label = self.browser.find_element_by_id('no_projects_label')
        self.assertEquals('Currently there are no projects to show.', label.text)

    def test_project_details_page_can_be_accessed_from_home_page(self):
        Project.objects.create(name='project1', summary='This is a fucking summary')
        self.go_to_projects()
        first_displayed_project = self.browser.find_elements_by_tag_name('a')[0]
        first_displayed_project.click()
        wait_for_page_to_load_with_id_or_fail(self, self.browser, 'name')

    def verify_projects_title_is_displayed(self):
        verify_page_h1_is_displayed(self, self.browser, 'Projects')

    def verify_projects_are_displayed(self):
        projects = Project.objects.all()
        displayed_projects = self.browser.find_elements_by_class_name('project')

        self.assertEqual(len(projects), len(displayed_projects))

        for index in range(len(projects)):
            project_name = displayed_projects[index].find_element_by_tag_name('li').text
            project_summary = displayed_projects[index].find_element_by_tag_name('p').text
            self.assertEqual(projects[index].name, project_name)
            self.assertEqual(projects[index].summary, project_summary)

    def navigate_to_projects(self):
        projects_link = self.browser.find_element_by_id('projects')
        projects_link.click()
        wait_for_page_to_load_with_id_or_fail(self, self.browser, 'projects_page_title')


class ProjectDetailsPageTest(StaticLiveServerTestCase):
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
