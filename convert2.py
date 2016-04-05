#!/usr/bin/python

import json

json_data=open('countries.json').read()
data = json.loads(json_data)

newdata={}

for d in data:
    newdata[d['name']['common']] = d['callingCode']


with open('country_phones.json', 'w') as outfile:
    json.dump(newdata, outfile, sort_keys=True, indent=2)
