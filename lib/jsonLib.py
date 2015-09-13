__author__ = 'rakesh.varma'

import json


class JsonLib:
    @staticmethod
    def updateJson(doc, **kwargs):
        json_doc = eval(doc)
        for key, value in kwargs.iteritems():
            json_doc[key] = value

        return json.dumps(json_doc)

    @staticmethod
    def deleteJson(doc, *args):
        json_doc = eval(doc)
        for key in args:
            del json_doc[key]

        return json.dumps(json_doc)
