from selenium import webdriver

from functional_tests.base import FunctionalTest
from projects.models import Project


class ProjectsPageTest(FunctionalTest):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def go_to_projects(self):
        self.driver.get(self.live_server_url + '/projects/')

    def test_projects_are_displayed(self):
        Project.objects.create(name='project1', summary='This is a fucking summary')
        Project.objects.create(name='project2', summary='This is a fucking summary')
        self.go_to_projects()
        self.verify_projects_are_displayed()
        Project.objects.all().delete()

    def test_label_is_displayed_when_no_projects_available(self):
        self.go_to_projects()

        label = self.driver.find_element_by_id('no_projects_label')
        self.assertEquals('Currently there are no projects to show.', label.text)

    def test_project_details_page_can_be_accessed_from_home_page(self):
        Project.objects.create(name='project1', summary='This is a fucking summary')
        self.go_to_projects()
        first_displayed_project = self.driver.find_elements_by_class_name('project')[0].find_element_by_tag_name('a')
        first_displayed_project.click()
        self.wait_for_page_to_load_with_id_or_fail('name')

    def verify_projects_title_is_displayed(self):
        self.verify_page_h1_is_displayed('Projects')

    def verify_projects_are_displayed(self):
        projects = Project.objects.all()
        displayed_projects = self.driver.find_elements_by_class_name('project')

        self.assertEqual(len(projects), len(displayed_projects))

        for index in range(len(projects)):
            project_name = displayed_projects[index].find_element_by_tag_name('li').text
            project_summary = displayed_projects[index].find_element_by_tag_name('p').text
            self.assertEqual(projects[index].name, project_name)
            self.assertEqual(projects[index].summary, project_summary)


class ProjectDetailsPageTest(FunctionalTest):
    def setUp(self):
        self.driver = webdriver.Chrome()
        Project.objects.create(
            name='project1',
            summary='This is a fucking summary',
            description='This is a really short description.'
        )
        self.project = Project.objects.all()[0]
        self.driver.get(self.live_server_url + '/projects/' + self.project.slug + '/')

    def test_project_details_are_displayed(self):
        self.verify_project_name()
        self.verify_status()
        self.verify_start_date()
        self.verify_description()

    def verify_description(self):
        description = self.driver.find_element_by_id('description')
        self.assertEqual(self.project.description, description.text)

    def verify_start_date(self):
        self.assertEqual('Start date: ' + self.project.get_start_date(),
                         self.driver.find_element_by_id('start_date').text)

    def verify_status(self):
        self.assertEqual('Status: ' + self.project.status,
                         self.driver.find_element_by_id('status').text)

    def verify_project_name(self):
        self.assertEqual(self.project.name, self.driver.find_element_by_id('name').text)
