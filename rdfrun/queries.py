from util import hodify
# structure:
# keys: names of queries, values: dictionary:
#                               keys: 'sparql','hod'
#                               values: actual queries
queries = {}
varorder = {}

#### QUERY 0

vavquery = {
    'sparql': """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX brick: <http://buildsys.org/ontologies/Brick#>
    PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
    SELECT DISTINCT ?vav WHERE {
        ?vav rdf:type brick:VAV .
    }""".strip(),
}
vavquery['hod'] = hodify(vavquery['sparql']).strip()

queries['enumerate vavs'] = vavquery
varorder['enumerate vavs'] = ['?vav']

#### QUERY 1

sensequery = {}
sensequery['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT DISTINCT ?sensor ?room WHERE {

    ?sensor rdf:type/rdfs:subClassOf* brick:Zone_Temperature_Sensor .
    ?room rdf:type brick:Room .
    ?vav rdf:type brick:VAV .
    ?zone rdf:type brick:HVAC_Zone .

    ?vav bf:feeds+ ?zone .
    ?zone bf:hasPart ?room .

    {?sensor bf:isPointOf ?vav }
    UNION
    {?sensor bf:isPointOf ?room }
}
""".strip()
sensequery['hod'] = """
SELECT ?sensor ?room WHERE {
    ?sensor rdf:type/rdfs:subClassOf* brick:Zone_Temperature_Sensor .
    ?room rdf:type brick:Room .
    ?vav rdf:type brick:VAV .
    ?zone rdf:type brick:HVAC_Zone .

    ?vav bf:feeds+ ?zone .
    ?zone bf:hasPart ?room .

    {
        {?sensor bf:isPointOf ?vav .}
        UNION
        {?sensor bf:isPointOf ?room .}
    }
};"""

queries['sensor to room and zone'] = sensequery
varorder['sensor to room and zone'] = ['?sensor','?room']

#### QUERY 2

valve = {}
valve['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?vlv_cmd ?vav WHERE {
    {
      { ?vlv_cmd rdf:type brick:Reheat_Valve_Command }
      UNION
      { ?vlv_cmd rdf:type brick:Cooling_Valve_Command }
    }
    ?vav rdf:type brick:VAV .
    ?vav bf:hasPoint+ ?vlv_cmd .
}""".strip()
valve['hod'] = """
SELECT ?vlv_cmd ?vav WHERE {
    {
      { ?vlv_cmd rdf:type brick:Reheat_Valve_Command . }
      UNION
      { ?vlv_cmd rdf:type brick:Cooling_Valve_Command . }
    }
    ?vav rdf:type brick:VAV .
    ?vav bf:hasPoint+ ?vlv_cmd .
};
"""

queries['vav valve query'] = valve
varorder['vav valve query'] = ['?vlv_cmd','?vav']


#### QUERY 3
spatial = {}
spatial['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?floor ?room ?zone WHERE {
    ?floor rdf:type brick:Floor .
    ?room rdf:type brick:Room .
    ?zone rdf:type brick:HVAC_Zone .

    ?room bf:isPartOf+ ?floor .
    ?room bf:isPartOf+ ?zone .
}
""".strip()
spatial['hod'] = hodify(spatial['sparql'])

queries['spatial layout query'] = spatial
varorder['spatial layout query'] = ['?floor','?room','?zone']
