__author__ = 'rakesh.varma'
import sys
sys.path.append('../lib/')
import unittest
from excelDataFileLib import *
from requestsLib import *
from testDataLib import *


class requestslib_tests(unittest.TestCase):

    def test_requestslib_no_header_response_code(self):
        url = "http://10.135.0.65:8085/api/effectiveapr"
        headers = {"HTTP-CORRELATION-ID" :'337fb81b-ef9a-4c1d-8f7e-e5f3ea2f6cb5', "Content-Type" : 'application/json'}
        e = {
                             "contract_date":"2015-07-01",
                             "first_payment_date":"2015-08-01",
                             "number_of_payments":36,
                             "amount_financed":79384.80,
                             "estimated_apr":0.0349,
                             "lender_fees":0,
                             "monthly_payment":2325.79,
                             "last_payment":2325.79
            }
        r = requestsLib(url = url, headers = headers, payload = e)
        self.assertEqual(r.response().status_code, 486)

    def test_requestslib_no_header_response_message(self):
        url = "http://10.135.0.65:8085/api/effectiveapr"
        e = {
                             "contract_date":"2015-07-01",
                             "first_payment_date":"2015-08-01",
                             "number_of_payments":36,
                             "amount_financed":79384.80,
                             "estimated_apr":0.0349,
                             "lender_fees":0,
                             "monthly_payment":2325.79,
                             "last_payment":2325.79
            }
        headers = {"HTTP-CORRELATION-ID" :'337fb81b-ef9a-4c1d-8f7e-e5f3ea2f6cb5', "Content-Type" : 'application/json'}
        r = requestsLib(url = url, headers = headers, payload = e)
        response = r.response().json()
        print response
        self.assertEqual(response['error']['message'], 'Invalid date order - First Payment Date must be greater than Contract Date')

    def test_compare_dict(self):
        dict1 = {'Name': 'Zara', 'Age': 7};
        dict2 = {'Name': 'Zara',   'Age': 7   };
        self.assertEqual(cmp(dict1, dict2), 0)
