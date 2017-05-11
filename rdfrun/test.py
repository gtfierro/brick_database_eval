from rdfrun import *

h = AlegroGraph()
print(queries['vav valve query']['sparql'])
res = h.query(queries['vav valve query']['sparql'])
print(res)


