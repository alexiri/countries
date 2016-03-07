#!/usr/bin/python
# coding=utf-8

import json

json_data=open('country_names.json').read()
data = json.loads(json_data)

# Ahora mismo los datos tienen esta pinta
# { 'Spain': ['ES', 'ESP', 'España', ...]
# 
# Hay que darles la vuelta, para que sea algo así:
# { 'ES': 'Spain',
#   'ESP': 'Spain',
#   'España': 'Spain', ...


nombres = {}

for d in data.keys():
    nombres[d.lower()] = d     # Añadimos el propio nombre del país, que así es más fácil luego
    for n in data[d]:
        nombres[n.lower()] = d


# Ahora buscar los nombres es trivial. Pon que tienes una columna con países, cada uno definido de una forma distinta

paises = ['ES', 'AW', 'AFG', 'ANGOLA', 'albanie', 'Andorran ruhtinaskunta']

# Puedes hacerlo así:

for p in paises:
    n = nombres.get(p.lower(), p)

    print "%s -> %s" % (p, n)
