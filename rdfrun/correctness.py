from rdfrun import *
import time

hod = HodDB()
fuseki = Fuseki()
alegro = AlegroGraph(init=False)
blaze = BlazeGraph()
rdf3x = RDF3X()
rdflib = RDFlib()

for queryname in queries.keys():
    print(queryname)
    order = varorder[queryname]
    qstr = queries[queryname]

    print("Run Hod")
    hod_res = hod.query(qstr['hod'], order)
    print("Run Fuseki")
    fuseki_res = fuseki.query(qstr['sparql'])
    print("Run Alegro")
    alegro_res = alegro.query(qstr['sparql'])
    print("Run Rdflib")
    rdf_res = rdflib.query(qstr['sparql'])
    print("Run Blazegraph")
    blaze_res = blaze.query(qstr['sparql'])

    hod_vs_rdf = set(hod_res).difference(set(rdf_res))
    hod_vs_fuseki = set(hod_res).difference(set(fuseki_res))
    hod_vs_alegro = set(hod_res).difference(set(alegro_res))
    hod_vs_blaze = set(hod_res).difference(set(blaze_res))

    print('Hod vs RDFLib', len(hod_vs_rdf))
    print('Hod vs Fuseki', len(hod_vs_fuseki))
    print('Hod vs Alegro', len(hod_vs_alegro))
    print('Hod vs Blaze', len(hod_vs_blaze))
