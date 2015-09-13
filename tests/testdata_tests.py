__author__ = 'rakesh.varma'
import unittest
import sys
sys.path.append('../')
from lib.testDataLib import *

class testdata_tests(unittest.TestCase):

    def test_inputdatafields_inheritance(self):
        input = TestDataInput(url = 'www.google.com', input = None, expectedOutput = None, expectedError = None, expectedHttpStatus = 200, testSummary = 'some test summary', testDescription  = 'some test description')
        self.assertEqual('www.google.com', input.url)

    def test_outputdatafields_inheritance(self):
        input = TestDataInput(url = 'www.google.com', input = None, expectedOutput = None, expectedError = None, expectedHttpStatus = 200, testSummary = 'some test summary', testDescription  = 'some test description')
        output = TestDataOutput(testDataInput = input, actualHttpStatus = 200, actualError = None, actualOutput = None)
        self.assertEqual('www.google.com', output.url)
        self.assertEqual(200, output.actualHttpStatus)
