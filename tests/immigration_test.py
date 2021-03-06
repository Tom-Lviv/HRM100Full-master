import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ImmigrationTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(
            executable_path='/Users/rcg/PycharmProjects/HRM100Full-master/browsers_drivers/chromedriver')
        self.driver.get("http://hrm-online.portnov.com/")
        self.wait = WebDriverWait(self.driver, 6)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_add_immigration_ts(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Immigration').click()
        driver.find_element_by_id('btnAdd').click()

        sleep(1)

        driver.find_element_by_id('immigration_number').clear()
        driver.find_element_by_id('immigration_number').send_keys('KAR9898989898')
        driver.find_element_by_id('immigration_country').send_keys('Italy')
        driver.find_element_by_id('immigration_i9_status').clear()
        driver.find_element_by_id('immigration_i9_status').send_keys("good_100%")

        sleep(1)

        driver.find_element_by_id('immigration_passport_issue_date').clear()
        driver.find_element_by_id('immigration_passport_issue_date').send_keys("04-16-2020")
        driver.find_element_by_id('immigration_i9_review_date').clear()
        driver.find_element_by_id('immigration_i9_review_date').send_keys("05-21-2020")
        driver.find_element_by_id('immigration_passport_expire_date').clear()
        driver.find_element_by_id('immigration_passport_expire_date').send_keys("07-31-2020")
        driver.find_element_by_id('immigration_comments').clear()
        driver.find_element_by_id('immigration_comments').send_keys("Fly 12-32-2020")
        driver.find_element_by_id('btnSave').click()

        sleep(2)
        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                           'Successfully Saved'))

    def test_immigration_vs(self):
        driver = self.driver

        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Immigration').click()
        driver.find_element_by_id('btnAdd').click()

        sleep(1)

        driver.find_element_by_id('immigration_type_flag_2').click()

        driver.find_element_by_id('immigration_number').clear()
        driver.find_element_by_id('immigration_number').send_keys('KAR9898989898')
        driver.find_element_by_id('immigration_country').send_keys('Italy')
        driver.find_element_by_id('immigration_i9_status').clear()
        driver.find_element_by_id('immigration_i9_status').send_keys("good_100%")

        sleep(1)
        driver.find_element_by_id('immigration_passport_issue_date').clear()
        driver.find_element_by_id('immigration_passport_issue_date').send_keys("04-16-2020")
        driver.find_element_by_id('immigration_i9_review_date').clear()
        driver.find_element_by_id('immigration_i9_review_date').send_keys("05-24-2020")
        driver.find_element_by_id('immigration_passport_expire_date').clear()
        driver.find_element_by_id('immigration_passport_expire_date').send_keys("07-31-2020")
        driver.find_element_by_id('immigration_comments').clear()
        driver.find_element_by_id('immigration_comments').send_keys("Fly 08-11-2020")
        driver.find_element_by_id('btnSave').click()

        sleep(1)

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))
        sleep(1)

        self.driver.find_element_by_css_selector('#immigrationCheckAll').click()
        self.driver.find_element_by_id('btnDelete').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Deleted'))
        sleep(1)

    def test_uploude_attachment_immigration(self):
        driver = self.driver
        driver.find_element_by_id('txtUsername').send_keys('admin')
        driver.find_element_by_id('txtPassword').send_keys('password')
        driver.find_element_by_id("btnLogin").click()

        sleep(1)

        driver.find_element_by_id('menu_pim_viewMyDetails').click()
        driver.find_element_by_link_text('Immigration').click()
        driver.find_element_by_id('btnAddAttachment').click()
        driver.find_element_by_id('ufile').send_keys('/Users/rcg/Desktop/HRM_photo/140kb.jpg')
        # driver.find_element_by_id('ufile').send_keys('/Users/rcg/Desktop/HRM_photo/900kb.png')
        # driver.find_element_by_id('ufile').send_keys('/Users/rcg/Desktop/HRM_photo/2_1Mb.jpg')

        sleep(1)

        self.driver.find_element_by_id('btnSaveAttachment').click()

        sleep(1)

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Saved'))
        sleep(1)

        self.driver.find_element_by_id('attachmentsCheckAll').click()
        self.driver.find_element_by_id('btnDeleteAttachment').click()

        self.wait.until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, ".message.success"),
                                                                          'Successfully Deleted'))
        sleep(1)

        self.assertTrue(True)
        ##############################


if __name__ == '__main__':
    unittest.main()
