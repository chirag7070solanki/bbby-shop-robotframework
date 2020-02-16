import unittest
import pytest_html
import testcases.l2plploading1
import testcases.l2plploading_nose
from unittest.suite import TestSuite
import nose


class CustomResultListener(unittest.TestResult):

    def startTest(self, test):
        print('Starting test : ', test)

    def stopTest(self, test):
        print('Stopping test : ', test)

    def addFailure(self, test, err):
        print("Failed test : ", test, " with error ", err)

    def addSuccess(self, test):
        print("Test passed : ", test)

    def addSkip(self, test, reason):
        print("Test skipped : ", test, "with reason : ", reason)

    def addExpectedFailure(self, test, err):
        print("Test Expected Failure : ", test, "with reason ", err)

    def addUnexpectedSuccess(self, test):
        print("Test UnExpected Passed : ", test)


if __name__ == "__main__":
    # load the test from test class
    tests = unittest.defaultTestLoader.loadTestsFromTestCase(testcases.l2plploading_nose.PlpLoading)
    # create object for result class we created
    custom_result = CustomResultListener()
    # load tests in to suite
    suite = TestSuite(tests)
    # run the suite
    final_result = suite.run(custom_result)
    unittest.main()
