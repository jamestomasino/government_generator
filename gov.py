#!/usr/local/bin/python

import json
json_data = open('gov.json')
data = json.load(json_data)

gov = data["government"];
types = [ x["name"] for x in gov]
print (types);
