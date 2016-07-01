import sys, unittest
from selenium import webdriver

sys.path.append("./")
from helper.helper import wait_for_page_to_load_with_id_or_fail
from helper.helper import verify_page_h1_is_displayed


class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/m/chromedriver')
        self.browser.get('http://localhost:8000')

    def tearDown(self):
        self.browser.quit()

    def test_projects_page_can_be_accessed_from_home_page(self):
        projects_link = self.browser.find_element_by_id('projects')
        projects_link.click()

        wait_for_page_to_load_with_id_or_fail(self, self.browser, 'projects_page_title')
        verify_page_h1_is_displayed(self, self.browser, 'Projects')

    def test_home_page_elements_are_displayed(self):
        self.verify_navigation_bar_elements_are_displayed()
        self.verify_skyglover_name_and_description_are_displayed()
        self.verify_get_in_touch_is_displayed()

    def verify_get_in_touch_is_displayed(self):
        self.browser.find_element_by_id('get_in_touch')

    def verify_skyglover_name_and_description_are_displayed(self):
        self.browser.find_element_by_id('skyglover_name')
        self.browser.find_element_by_id('skyglover_description')

    def verify_navigation_bar_elements_are_displayed(self):
        self.browser.find_element_by_id('projects')
        self.browser.find_element_by_id('team')
        self.browser.find_element_by_id('about')


if __name__ == "__main__":
    unittest.main(warnings='ignore')
