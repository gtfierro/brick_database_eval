from rdfrun import *

hod = HodDB()
rdflib = RDFlib()

for queryname in queries.keys():
    print(queryname)
    order = varorder[queryname]
    qstr = queries[queryname]

    hod_res = hod.query(qstr['hod'], order)
    rdf_res = rdflib.query(qstr['sparql'])
    print(set(hod_res).difference(set(rdf_res)))
