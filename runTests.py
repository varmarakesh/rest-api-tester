__author__ = 'rakesh.varma'
from lib.excelDataFileLib import *
from lib.testDataLib import *
from lib.requestsLib import *
from os import *
from ConfigParser import *
import os, glob

def getConfigSetting(setting):
    config_parser = SafeConfigParser()
    config_parser.read('config.ini')
    return config_parser.get('default',setting)

def runTests():
    test_dir = getConfigSetting('testdata_directory_path')
    headers = getConfigSetting('headers')
    os.chdir(test_dir)
    for f in glob.glob("*.xlsx"):
        print 'Found input file {0} in directory {1}'. format(f, test_dir)
        testdata_file = os.path.join(test_dir, f)
        xl = excelDataFileLib(testInputDataFile = testdata_file)
        xl.loadTestData()
        inputs = xl.testDataInputs
        results = []
        for e in inputs:
            response = requestsLib(url = e.url, headers = eval(headers), payload = e.input).response()
            testResult = TestDataOutput(e, actualOutput = json.dumps(response.json()), actualHttpStatus = response.status_code, actualError = None)
            results.append(testResult)
        xl.writeTestDataResults(testDataResults = results)
        print 'Completed {0} tests. Written results to {1}'.format(results.__len__(), xl.getResultsFilePath())

if __name__ == "__main__":
    runTests()
