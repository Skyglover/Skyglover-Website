from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_page_to_load_with_id_or_fail(test_case, web_driver, page_id, time_to_wait=10):
    try:
        WebDriverWait(web_driver, time_to_wait).until(
            expected_conditions.presence_of_element_located((By.ID, page_id)))
    except TimeoutException:
        test_case.fail("Page took too much time to load!")


def verify_page_h1_is_displayed(test_case, web_driver, title):
    test_case.assertEqual(title, web_driver.find_element_by_tag_name('h1').text)


def assert_path_uses_template(test_case, path, template):
    response = test_case.client.get(path)
    test_case.assertTemplateUsed(response, template)
