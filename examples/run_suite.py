from xunit.testresult import TestResult
from xunit.testsuite import TestSuite
from examples.test_testcase import TestCaseTest
from examples.test_testsuite import TestSuiteTest

if __name__ == "__main__":
    result = TestResult()
    suite = TestSuite()

    suite.add_test(TestCaseTest("test_result_success_run"))
    suite.add_test(TestCaseTest("test_result_failure_run"))
    suite.add_test(TestCaseTest("test_result_error_run"))
    suite.add_test(TestCaseTest("test_result_multiple_run"))
    suite.add_test(TestCaseTest("test_was_set_up"))
    suite.add_test(TestCaseTest("test_was_run"))
    suite.add_test(TestCaseTest("test_was_tear_down"))
    suite.add_test(TestCaseTest("test_template_method"))

    suite.add_test(TestSuiteTest("test_suite_size"))
    suite.add_test(TestSuiteTest("test_suite_success_run"))
    suite.add_test(TestSuiteTest("test_suite_multiple_run"))

    suite.run(result)
    print(result.summary())
