import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(
            executable_path='/Users/rcg/PycharmProjects/HRM100Full-master/browsers_drivers/chromedriver')
        self.driver.get("http://hrm-online.portnov.com/")
        self.wait = WebDriverWait(self.driver, 6)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_job_details(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_elements_by_link_text('Job').click()

        driver.find_elements_by_link_text('Job Title').click.send_keys()
        driver.find_elements_by_id()

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
