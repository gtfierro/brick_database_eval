import flask
import json
from flask import request
import rdflib

app = flask.Flask(__name__)

RDF = rdflib.Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = rdflib.Namespace('http://www.w3.org/2000/01/rdf-schema#')
BRICK = rdflib.Namespace('http://buildsys.org/ontologies/Brick#')
BRICKFRAME = rdflib.Namespace('http://buildsys.org/ontologies/BrickFrame#')
BRICKTAG = rdflib.Namespace('http://buildsys.org/ontologies/BrickTag#')
OWL = rdflib.Namespace('http://www.w3.org/2002/07/owl#')
g = rdflib.Graph(store="Sleepycat",identifier='datag')
g.open('./datag', create = True)
g.bind( 'rdf', RDF)
g.bind( 'rdfs', RDFS)
g.bind( 'brick', BRICK)
g.bind( 'bf', BRICKFRAME)
g.bind( 'btag', BRICKTAG)
g.bind( 'owl', OWL)
pfx = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
"""
g.parse('../Brick.ttl', format='turtle')
g.parse('../BrickFrame.ttl', format='turtle')
g.parse('../berkeley.ttl', format='turtle')
# ADD INVERSE RELATIONSHIPS
res = g.query(pfx+"SELECT ?a ?b WHERE { ?a bf:hasPart ?b .}")
for row in res:
    g.add((row[1], BRICKFRAME.isPartOf, row[0]))
res = g.query(pfx+"SELECT ?a ?b WHERE { ?a bf:isPartOf ?b .}")
for row in res:
    g.add((row[1], BRICKFRAME.hasPart, row[0]))

res = g.query(pfx+"SELECT ?a ?b WHERE {?a bf:hasPoint ?b .}")
for row in res:
    g.add((row[1], BRICKFRAME.isPointOf, row[0]))
res = g.query(pfx+"SELECT ?a ?b WHERE {?a bf:isPointOf ?b .}")
for row in res:
    g.add((row[1], BRICKFRAME.hasPoint, row[0]))

res = g.query(pfx+"SELECT ?a ?b WHERE {?a bf:feeds ?b .}")
for row in res:
    g.add((row[1], BRICKFRAME.isFedBy, row[0]))
res = g.query(pfx+"SELECT ?a ?b WHERE {?a bf:isFedBy ?b .}")
for row in res:
    g.add((row[1], BRICKFRAME.feeds, row[0]))

res = g.query(pfx+"SELECT ?a ?b WHERE {?a bf:contains ?b .}")
for row in res:
    g.add((row[1], BRICKFRAME.isLocatedIn, row[0]))
res = g.query(pfx+"SELECT ?a ?b WHERE {?a bf:isLocatedIn ?b .}")
for row in res:
    g.add((row[1], BRICKFRAME.contains, row[0]))

res = g.query(pfx+"SELECT ?a ?b WHERE {?a bf:controls ?b .}")
for row in res:
    g.add((row[1], BRICKFRAME.isControlledBy, row[0]))
res = g.query(pfx+"SELECT ?a ?b WHERE {?a bf:isControlledBy ?b .}")
for row in res:
    g.add((row[1], BRICKFRAME.controls, row[0]))

res = g.query(pfx+"SELECT ?a ?b WHERE {?a bf:hasOutput ?b .}")
for row in res:
    g.add((row[1], BRICKFRAME.isOutputOf, row[0]))

res = g.query(pfx+"SELECT ?a ?b WHERE {?a bf:hasInput ?b .}")
for row in res:
    g.add((row[1], BRICKFRAME.isInputOf, row[0]))

res = g.query(pfx+"SELECT ?a ?b WHERE {?a bf:hasTagSet ?b .}")
for row in res:
    g.add((row[1], BRICKFRAME.isTagSetOf, row[0]))

res = g.query(pfx+"SELECT ?a ?b WHERE {?a bf:hasToken ?b .}")
for row in res:
    g.add((row[1], BRICKFRAME.isTokenOf, row[0]))


@app.route('/query',methods=['POST'])
def query():
    q = request.form['query']
    res = g.query(q)
    return json.dumps(list(res))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, threaded=True)
