# -*- coding: utf-8 -*-
import sys
import HTMLTestRunner
import time
from createTestSuite import CreateTestSuites as CTS

def run_up():
    # 如果参数为all，调用create_test_suites_by_path。如果参数为list，调用create_test_suites_by_list。
    try:
        if sys.argv[1] == 'all':
            top_path = r'.\\testSuites'
            test_suites = CTS().create_test_suites_by_path(top_path)
        elif sys.argv[1] == 'list':
            list_file = r'.\\suitesList'
            test_suites = CTS().create_test_suites_by_list(list_file)
        else:
            print "[ERROR]: params only can be 'all' or 'list'"
            return
    except IndexError:
        print "[ERROR]: Please input params, like 'python AutoUITest all' or 'python AutoUITest list'"
        return

    # 定义测试报告
    current_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    report_file = r'.\\testReport\\' + current_time + '_TestReport.html'
    fp = file(report_file, 'wb+')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='TestReport', description='TestReport Info:')

    runner.run(test_suites)

if __name__ == '__main__':
    run_up()
