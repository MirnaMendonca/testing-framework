from xunit.testloader import TestLoader
from xunit.testsuite import TestSuite
from xunit.testrunner import TestRunner
from examples.test_testcase import TestCaseTest
from examples.test_testsuite import TestSuiteTest
from examples.test_testloader import TestLoaderTest

if __name__ == "__main__":
    loader = TestLoader()
    test_case_suite = loader.make_suite(TestCaseTest)
    test_suite_suite = loader.make_suite(TestSuiteTest)
    test_load_suite = loader.make_suite(TestLoaderTest)

    suite = TestSuite()
    suite.add_test(test_case_suite)
    suite.add_test(test_suite_suite)
    suite.add_test(test_load_suite)

    runner = TestRunner()
    runner.run(suite)
