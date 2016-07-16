from selenium import webdriver

from functional_tests.base import FunctionalTest
from home.models import SomeText


class HomePageTest(FunctionalTest):

    def test_home_page_elements_are_displayed(self):
        self.verify_navigation_bar_elements_are_displayed()
        self.verify_skyglover_name_and_description_are_displayed()
        self.verify_get_in_touch_is_displayed()

    def test_projects_page_can_be_accessed_from_home_page(self):
        self.click_on_link_with_id('projects')
        self.wait_for_page_to_load_with_id_or_fail('projects')
        projects_button = self.driver.find_element_by_class_name('active').find_element_by_id('projects')
        self.assertEqual('Projects', projects_button.text)

    def test_team_page_can_be_accessed_from_home_page(self):
        self.click_on_link_with_id('team')
        self.wait_for_page_to_load_with_id_or_fail('team_page_title')

    def test_about_page_can_be_access_from_home_page(self):
        SomeText.objects.create(identifier='about_info', text='We are Skyglover')
        self.click_on_link_with_id('about')
        self.wait_for_page_to_load_with_id_or_fail('about_page_title')

    def test_get_in_touch_page_can_be_access_from_home_page(self):
        self.click_on_link_with_id('get_in_touch')
        self.wait_for_page_to_load_with_id_or_fail('get_in_touch_page_title')

    def click_on_link_with_id(self, link_id):
        projects_link = self.driver.find_element_by_id(link_id)
        projects_link.click()

    def verify_get_in_touch_is_displayed(self):
        get_in_touch = self.driver.find_element_by_id('get_in_touch')
        self.assertEqual('Get in touch', get_in_touch.text)

    def verify_skyglover_name_and_description_are_displayed(self):
        skyglover_name = self.driver.find_element_by_id('skyglover_name')
        skyglover_description = self.driver.find_element_by_id('skyglover_description')
        self.assertEqual('skyglover', skyglover_name.text)
        self.assertEqual('We are a video game and mobile application company.',
                         skyglover_description.text)

    def verify_navigation_bar_elements_are_displayed(self):
        projects_link = self.driver.find_element_by_id('projects')
        team_link = self.driver.find_element_by_id('team')
        about_link = self.driver.find_element_by_id('about')
        self.assertEqual('Projects', projects_link.text)
        self.assertEqual('Team', team_link.text)
        self.assertEqual('About', about_link.text)


class AboutPageTest(FunctionalTest):
    def setUp(self):
        SomeText.objects.create(identifier='about_info', text='We are Skyglover')
        self.driver = webdriver.Chrome()
        self.driver.get(self.live_server_url + '/about/')

    def test_about_page_elements_are_displayed(self):
        self.verify_page_h1_is_displayed('About')
        self.verify_about_information_is_displayed()

    def verify_about_information_is_displayed(self):
        about_information = SomeText.objects.all().get(identifier='about_info').text
        about_information_displayed = self.driver.find_element_by_tag_name('p')
        self.assertEqual(about_information, about_information_displayed.text)


class GetInTouchPageTest(FunctionalTest):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.live_server_url + '/get-in-touch/')

    def test_get_in_touch_page_elements_are_displayed(self):
        self.verify_page_h1_is_displayed('Get In Touch')
        twitter = self.driver.find_element_by_id('twitter').text
        github = self.driver.find_element_by_id('github').text
        email = self.driver.find_element_by_id('email').text
        address = self.driver.find_element_by_tag_name('footer').text
        self.assertEqual('Twitter', twitter)
        self.assertEqual('Github', github)
        self.assertEqual('Email', email)
        self.assertEqual('Quito, Ecuador', address)
