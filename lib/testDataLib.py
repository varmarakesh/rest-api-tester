__author__ = 'rakesh.varma'

import ast
import json

class TestData:
    url = None
    input = None
    expectedOutput = None
    expectedHttpStatus = None
    expectedError = None
    testSummary = None
    testDescription = None


class TestDataInput(TestData):
    def __init__(self, url, input, expectedOutput, expectedHttpStatus, expectedError, testSummary, testDescription):
        self.url = url
        self.input = input
        self.expectedOutput = expectedOutput
        self.expectedHttpStatus = expectedHttpStatus
        self.expectedError = expectedError
        self.testSummary = testSummary
        self.testDescription = testDescription


class TestDataOutput(TestDataInput):
    actualOutput = None
    actualHttpStatus = None
    actualError = None
    result = 'FAIL'

    def _json_compare(self, json1, json2):
        if ((json1 is None) and (json2 is None)):
            return True
        else:
            return json.loads(json1) == json.loads(json2)

    def __init__(self, testDataInput, actualOutput, actualHttpStatus, actualError):
        TestDataInput.__init__(self, url = testDataInput.url, input = testDataInput.input, expectedOutput = testDataInput.expectedOutput, expectedError = testDataInput.expectedError,
                               expectedHttpStatus = testDataInput.expectedHttpStatus, testSummary = testDataInput.testSummary, testDescription = testDataInput.testDescription)
        self.actualOutput = actualOutput
        self.actualHttpStatus = actualHttpStatus
        self.actualError = actualError
        if (self.expectedHttpStatus == 200 and self.actualHttpStatus == 200):
            self.result = 'PASS' if (self._json_compare(self.expectedOutput, self.actualOutput)) else 'FAIL'
        else:
            self.result = 'PASS' if (self.expectedHttpStatus == self.actualHttpStatus) else 'FAIL'