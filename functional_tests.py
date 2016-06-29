import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/m/chromedriver')

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main(warnings='ignore')
