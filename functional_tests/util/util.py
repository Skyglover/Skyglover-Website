from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_page_to_load_with_id(web_driver, page_id, time_to_wait=10):
    WebDriverWait(web_driver, time_to_wait).until(
        expected_conditions.presence_of_element_located((By.ID, page_id))
    )
