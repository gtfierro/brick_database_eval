from rdfrun import *

#b = AlegroGraph()
#print(queries['spatial layout query']['sparql'])
#res_b = b.query(queries['spatial layout query']['sparql'])

h = HodDB()
print(queries['spatial layout query']['hod'])
res_h = h.query(queries['spatial layout query']['hod'], varorder['spatial layout query'])

#print(set(res_h).difference(set(res_b)))

#print(queries['vav valve query']['sparql'])
#res = h.query(queries['vav valve query']['sparql'])
#print(res)
#
#print(queries['enumerate vavs']['sparql'])
#res = h.query(queries['enumerate vavs']['sparql'])
#print(res)
