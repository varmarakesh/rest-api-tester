# README #

This project automates the testing of the REST API's. Currently it works for REST API's that use http post with a json payload and response. For testing rest api's, normally this
is the testing methodology to determine if a certain test passes.

1. For a certain request ensure you get the desired output response - Validate the response body
2. For a certain request ensure you get the desired http response status - Validate the response http status.
3. For a certain request that generates a fault ensure that you get the desired response - Validate the error/fault in the response body.


You can build an excel input file that has the url, expected http status and input json,
and runTests.py will generate HTTP requests using requests library and compare the expected inputs with the actual results and determines if the tests passed or failed.

Refer to the sample xml file in the testdata/ directory for the format of the input file.

To install and run this project, follow the instructions.

1. Clone the repository.
git clone https://github.dev.dealertrack.com/DT2-CalcServices/calc-api-tests.git
2. Install the necessary libraries with the specified versions, suggest to create a virtualenv.
    cd /calc_api_tests/build
    pip install -r requirements.txt
4. In config.ini, update your testdata_directory_path to the directory path where your testdata will reside, update the http headers (eg: authentication, content-type).
4. python runTests.py
5. Check the results directory, for each xlsx file in the testdata, a results file will be created in the results directory.

This has been tested so far using.
python 2.7
mac osx 10.9.5
centos 7


