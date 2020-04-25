import json
import xml

class JSONParser:
    def parse(self, raw_data):
        return json.loads(raw_data)


class XMLParser:
    def parse(self, raw_data):
        return xml(raw_data)


def new_parser(type, **kwargs):
    if type == 'json':
        return JSONParser()
    elif type == 'xml':
        return XMLParser()


parser = new_parser('json')
with open('hello.json') as fp:
    data = parser.parse(fp.read())
print(data)