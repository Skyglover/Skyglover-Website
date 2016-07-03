import sys, unittest
from selenium import webdriver

sys.path.append("./")
from helper.helper import wait_for_page_to_load_with_id_or_fail


class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/m/chromedriver')
        self.browser.get('http://localhost:8000')

    def tearDown(self):
        self.browser.quit()

    def test_home_page_elements_are_displayed(self):
        self.verify_navigation_bar_elements_are_displayed()
        self.verify_skyglover_name_and_description_are_displayed()
        self.verify_get_in_touch_is_displayed()

    def test_projects_page_can_be_accessed_from_home_page(self):
        self.click_on_link_with_id('projects')
        wait_for_page_to_load_with_id_or_fail(self, self.browser, 'projects_page_title')

    def test_team_page_can_be_accessed_from_home_page(self):
        self.click_on_link_with_id('team')
        wait_for_page_to_load_with_id_or_fail(self, self.browser, 'team_page_title')

    def test_about_page_can_be_access_from_home_page(self):
        self.click_on_link_with_id('about')
        wait_for_page_to_load_with_id_or_fail(self, self.browser, 'about_page_title')

    def test_get_in_touch_page_can_be_access_from_home_page(self):
        self.click_on_link_with_id('get_in_touch')
        wait_for_page_to_load_with_id_or_fail(self, self.browser, 'get_in_touch_page_title')

    def click_on_link_with_id(self, link_id):
        projects_link = self.browser.find_element_by_id(link_id)
        projects_link.click()

    def verify_get_in_touch_is_displayed(self):
        get_in_touch = self.browser.find_element_by_id('get_in_touch')
        self.assertEqual('Get in touch', get_in_touch.text)

    def verify_skyglover_name_and_description_are_displayed(self):
        skyglover_name = self.browser.find_element_by_id('skyglover_name')
        skyglover_description = self.browser.find_element_by_id('skyglover_description')
        self.assertEqual('skyglover', skyglover_name.text)
        self.assertEqual('We are a video game and mobile application company.',
                         skyglover_description.text)

    def verify_navigation_bar_elements_are_displayed(self):
        projects_link = self.browser.find_element_by_id('projects')
        team_link = self.browser.find_element_by_id('team')
        about_link = self.browser.find_element_by_id('about')
        self.assertEqual('Projects', projects_link.text)
        self.assertEqual('Team', team_link.text)
        self.assertEqual('About', about_link.text)


if __name__ == "__main__":
    unittest.main(warnings='ignore')
