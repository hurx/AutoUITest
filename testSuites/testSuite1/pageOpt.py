# -*- coding:utf-8 -*-

class PageOpt:
    def __init__(self, driver):
        self.driver = driver

    def options(self, **args):
        if args["user_name"] is None:
            pass
        else:
            self.driver.find_element_by_id("input_user_name").send_keys(args["user_name"])
        if args["pass_word"] is None:
            pass
        else:
            self.driver.find_element_by_id("input_user_pwd").send_keys(args["pass_word"])
        if args["submit"] is None:
            pass
        else:
            self.driver.find_element_by_id("login_btn").click()
