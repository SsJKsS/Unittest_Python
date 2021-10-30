from selenium import webdriver
import time
from time import sleep
import unittest
from poium import Page, Element
from selenium.webdriver import Chrome
from HTMLReport import ddt, TestRunner, addImage, no_retry, retry
from page.google_page import GooglePage
import logging


class Teaches(unittest.TestCase):
    def is_element_exist(self, element):
        source = self.driver.page_source
        if element in source:
            return True
        else:
            return False

    # initial setting
    def setUp(self):
        self.driver = webdriver.Chrome()

# 【後台】登入頁面欄位、邏輯
    def test_a(self):
        # noinspection PyBroadException
        try:
            page = GooglePage(self.driver)
            page.open('https://www.google.com/')
            self.driver.maximize_window()
            sleep(1)
            page.Search_bar.send_keys("OK")
            sleep(1)
            logging.info('測試 1 通過!')
            page.Search_bar.send_keys("OK")
            page.Search_button.click()
            sleep(1)
            logging.info('測試 2 通過!')

        except:
            flag = False
            if flag is False or Exception:
                self.driver.save_screenshot('screenshot/frontStartCourse_Fail_{}.png'.format(current_time))
                self.assertTrue(flag, 'Execute Fail.')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    test_runner = TestRunner(
        report_file_name='report_' + current_time,
        output_path="report",
        title="Happy",
        description="Haha",
        sequential_execution=True,
        lang="en"
    )
    suite = unittest.TestSuite()
    suite.addTest(Teaches('test_a'))
    test_runner.run(suite)
