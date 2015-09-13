__author__ = 'rakesh.varma'
import sys
import unittest
from os import *
import os
import glob
sys.path.append('../')

class runTests(unittest.TestCase):

    def test_testdata_contents_read(self):
        count = 0
        filepath = '/Users/rakesh.varma/bitbucket/calc_api_tests/testdata/'
        self.assertEqual('/Users/rakesh.varma/bitbucket/calc_api_tests/testdata/CalcApiTestInputData.xlsx', os.path.join(filepath, listdir(filepath)[0]))

    def test_glob_dir(self):
        filepath = '/Users/rakesh.varma/bitbucket/calc_api_tests/testdata/'
        os.chdir(filepath)
        input_files = glob.glob("*.xlsx")
        self.assertEqual(input_files.__len__(),2)
