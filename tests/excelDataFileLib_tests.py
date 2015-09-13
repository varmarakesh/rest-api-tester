__author__ = 'rakesh.varma'
import unittest
import sys, os
sys.path.append('../lib')
from excelDataFileLib import *

class excelDataFileLib_tests(unittest.TestCase):

    def setUp(self):
        self.inputCsvFile = "/Users/rakesh.varma/bitbucket/calc_api_tests/testdata/drs_dev_calc_api_tests.xlsx"


    def test_excel_file_header_read(self):
        wb = openpyxl.load_workbook(self.inputCsvFile)
        sheet = wb.get_active_sheet()
        self.assertEqual(sheet['A1'].value, 'URL')

    def test_excel_file_body_read(self):
        wb = openpyxl.load_workbook(self.inputCsvFile)
        sheet = wb.get_active_sheet()
        val = sheet.cell(row = 2, column = 1).value
        self.assertEqual(val, "http://10.136.14.13:8076/api/effectiveapr")

    def test_loadtestdata(self):
        xl = excelDataFileLib(self.inputCsvFile)
        xl.loadTestData()
        self.assertEqual("http://10.136.14.13:8076/api/effectiveapr", xl.testDataInputs[0].url)

    def test_filepath_parse(self):
        dir, file = os.path.split(self.inputCsvFile)
        self.assertEqual(dir, '/Users/rakesh.varma/bitbucket/calc_api_tests/testdata')
        self.assertEqual(file, 'drs_dev_calc_api_tests.xlsx')
        parent_dir = os.path.split(os.path.dirname(self.inputCsvFile))[0]
        self.assertEqual("/Users/rakesh.varma/bitbucket/calc_api_tests", parent_dir)

    def test_result_file_name(self):
          xl = excelDataFileLib(testInputDataFile = self.inputCsvFile)
          self.assertEqual(xl.getResultsFilePath(), "/Users/rakesh.varma/bitbucket/calc_api_tests/results/drs_dev_calc_api_tests_results.xlsx")

