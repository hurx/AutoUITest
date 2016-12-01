# -*- coding:utf-8 -*-

import unittest
from selenium import webdriver
from pageOpt import PageOpt

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.1.1.122:8080/login.do"
        self.driver.get(self.base_url)
        self.page_opt = PageOpt(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_success(self):
        u"""成功案例"""
        args = {
            "user_name": "waangxiaolingan8",
            "pass_word": '111111',
            "submit": '1'
        }
        self.page_opt.options(**args)


if __name__ == "__main__":
    unittest.main()
