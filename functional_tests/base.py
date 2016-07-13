from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.live_server_url)

    def tearDown(self):
        self.driver.quit()

    def wait_for_page_to_load_with_id_or_fail(self, page_id, time_to_wait=10):
        try:
            WebDriverWait(self.driver, time_to_wait).until(
                expected_conditions.presence_of_element_located((By.ID, page_id)))
        except TimeoutException:
            self.fail("Page took too much time to load!")

    def verify_page_h1_is_displayed(self, title):
        self.assertEqual(title, self.driver.find_element_by_tag_name('h1').text)

    def assert_path_uses_template(self, path, template):
        response = self.client.get(path)
        self.assertTemplateUsed(response, template)
