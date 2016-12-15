import requests
import json
import rdflib

RDF = rdflib.Namespace('http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = rdflib.Namespace('http://www.w3.org/2000/01/rdf-schema#')
BRICK = rdflib.Namespace('http://buildsys.org/ontologies/Brick#')
BRICKFRAME = rdflib.Namespace('http://buildsys.org/ontologies/BrickFrame#')
BRICKTAG = rdflib.Namespace('http://buildsys.org/ontologies/BrickTag#')
OWL = rdflib.Namespace('http://www.w3.org/2002/07/owl#')
g = rdflib.Graph()
g.bind( 'rdf', RDF)
g.bind( 'rdfs', RDFS)
g.bind( 'brick', BRICK)
g.bind( 'bf', BRICKFRAME)
g.bind( 'btag', BRICKTAG)
g.bind( 'owl', OWL)
g.parse('../Brick.ttl', format='turtle')
g.parse('../BrickFrame.ttl', format='turtle')
g.parse('../berkeley.ttl', format='turtle')

objs = []
for trip in g:
    o = {'s': trip[0], 'p': trip[1], 'o': trip[2], 'c': ''}
    objs.append(o)
