__author__ = 'rakesh.varma'
import sys
sys.path.append('../lib/')
sys.path.append('../')
import unittest
from excelDataFileLib import *
from requestsLib import *
from testDataLib import *
from runTests import *


class completeTests(unittest.TestCase):

    def setUp(self):
        self.inputCsvFile = "/Users/rakesh.varma/bitbucket/calc_api_tests/testdata/drs_dev_calc_api_tests.xlsx"


    def test_invokerequest_compare(self):
        xl = excelDataFileLib(self.inputCsvFile)
        xl.loadTestData()
        r = requests.post(xl.testDataInputs[0].url,
                          headers = {"HTTP-CORRELATION-ID" :'337fb81b-ef9a-4c1d-8f7e-e5f3ea2f6cb5', "Content-Type" : 'application/json'},
                            data = xl.testDataInputs[0].input)
        response = r.json()
        self.assertEqual(response, ast.literal_eval(xl.testDataInputs[0].expectedOutput))


    def test_advancedtest_fields(self):
        xl = excelDataFileLib(testInputDataFile = self.inputCsvFile)
        xl.loadTestData()
        e = xl.testDataInputs[0]
        response = requestsLib(url = e.url, payload = e.input).response()
        self.assertEqual(e.url, response.url)
        self.assertEqual(response.status_code, e.expectedHttpStatus)
        self.assertEqual(response.json(),ast.literal_eval(e.expectedOutput))


    def test_results_count(self):
        xl = excelDataFileLib(testInputDataFile = self.inputCsvFile)
        xl.loadTestData()
        inputs = xl.testDataInputs
        results = []
        for e in inputs:
            response = requestsLib(url = e.url, payload = e.input).response()
            testResult = TestDataOutput(e, actualOutput = json.dumps(response.json()), actualHttpStatus = response.status_code, actualError = None)
            results.append(testResult)

        wb = openpyxl.load_workbook(self.inputCsvFile)
        sheet = wb.get_active_sheet()
        self.assertEqual(results.__len__(),sheet.get_highest_row()-1)


    def test_write_excel_body(self):
        xl = excelDataFileLib(testInputDataFile = self.inputCsvFile)
        xl.loadTestData()
        inputs = xl.testDataInputs
        results = []
        for e in inputs:
            response = requestsLib(url = e.url, payload = e.input).response()
            testResult = TestDataOutput(e, actualOutput = json.dumps(response.json()), actualHttpStatus = response.status_code, actualError = None)
            results.append(testResult)
        xl.writeTestDataResults(testDataResults = results)
        outfile = xl.getResultsFilePath()
        wb = openpyxl.load_workbook(outfile)
        sheet = wb.get_active_sheet()
        self.assertEqual(sheet.cell(row = 2, column = 1).value, results[0].url)
        self.assertEqual(sheet.cell(row = 2, column = 4).value, results[0].expectedHttpStatus)
        self.assertEqual(sheet.cell(row = 2, column = 5).value, results[0].expectedError)
        self.assertEqual(sheet.cell(row = 2, column = 7).value, results[0].actualHttpStatus)
        self.assertEqual(sheet.cell(row = 2, column = 8).value, results[0].actualError)

    def test_compare_jsons_type(self):
        xl = excelDataFileLib(testInputDataFile = self.inputCsvFile)
        xl.loadTestData()
        inputs = xl.testDataInputs
        results = []
        for e in inputs:
            response = requestsLib(url = e.url, payload = e.input).response()
            testResult = TestDataOutput(e, actualOutput = json.dumps(response.json()), actualHttpStatus = response.status_code, actualError = None)
            results.append(testResult)

        dict1 = json.loads(results[0].actualOutput)
        dict2 =  json.loads(results[0].expectedOutput)

        self.assertEqual(cmp(dict1, dict2), 0)

    def test_runtests(self):
        runTests()
        self.assertEqual(1,1)