from src.core.test_loader import TestLoader
from src.core.test_suite import TestSuite
from src.core.test_runner import TestRunner

from test.test_case_test import TestCaseTest
from test.test_suite_test import TestSuiteTest
from test.test_loader_test import TestLoaderTest


if __name__ == "__main__":
    loader = TestLoader()

    test_case_suite = loader.make_suite(TestCaseTest)
    test_suite_suite = loader.make_suite(TestSuiteTest)
    test_loader_suite = loader.make_suite(TestLoaderTest)

    master_suite = TestSuite()
    master_suite.add_test(test_case_suite)
    master_suite.add_test(test_suite_suite)
    master_suite.add_test(test_loader_suite)

    runner = TestRunner()
    runner.run(master_suite)
