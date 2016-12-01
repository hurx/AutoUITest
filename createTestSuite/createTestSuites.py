# -*- coding: utf-8 -*-
import unittest

class CreateTestSuites:
    def __init__(self):
        self.test_suites = unittest.TestSuite()

    def create_test_suites_by_path(self, test_suites_path):
        # 定义discover方法:找到指定目录下所有测试模块，并可递归查到子目录下的测试模块。
        # 只有匹配到文件名才能被加载。如果启动的不是顶层目录，那么顶层目录必须要单独指定。
        discover = unittest.defaultTestLoader.discover(test_suites_path,
                                                       pattern='test*.py',
                                                       top_level_dir=None)
        for test_suite in discover:
            for test_case in test_suite:
                    self.test_suites.addTest(test_case)
        return self.test_suites

    def create_test_suites_by_list(self, case_list_file):
        fp = open(case_list_file, 'r')
        lines = fp.readlines()
        for line in lines:
            test_case = line.split(',')
            import_str = "from testSuites.%s import %s" % (test_case[0], test_case[1])
            exec import_str
            self.test_suites.addTest(unittest.makeSuite(eval(test_case[1])))
        return self.test_suites
