#!/usr/bin/python

import json

json_data=open('countries.json').read()
data = json.loads(json_data)

newdata={}

for d in data:
    names = set()

    names.add(d['name']['official'])
    names.add(d['cca2'])
    names.add(d['cca3'])
    names.add(d['cioc'])

    for n in d['altSpellings']:
        names.add(n)

    for n in d['name']['native']:
        names.add(d['name']['native'][n]['common'])
        names.add(d['name']['native'][n]['official'])

    for n in d['translations']:
        names.add(d['translations'][n]['common'])
        names.add(d['translations'][n]['official'])

    newdata[d['name']['common']] = sorted([x for x in names if x])


with open('country_names.json', 'w') as outfile:
    json.dump(newdata, outfile, sort_keys=True, indent=2)
