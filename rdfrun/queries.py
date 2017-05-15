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


#### QUERY 4
q4 = {}
q4['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?x WHERE { ?x rdf:type brick:Room . }
""".strip()
q4['hod'] = hodify(q4['sparql'])

queries['room enumerate'] = q4
varorder['room enumerate'] = ['?x']


#### QUERY 5
q5 = {}
q5['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?vav ?room WHERE {
    ?vav rdf:type brick:VAV .
    ?room rdf:type brick:Room .
    ?zone rdf:type brick:HVAC_Zone .
    ?vav bf:feeds+ ?zone .
    ?room bf:isPartOf ?zone .
}
""".strip()
q5['hod'] = hodify(q5['sparql'])

queries['vav/room/zone'] = q5
varorder['vav/room/zone'] = ['?vav', '?room']

#### QUERY 6
q6 = {}
q6['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?pred ?obj WHERE {
    ?vav rdf:type brick:VAV .
    ?vav ?pred ?obj .
}
""".strip()
q6['hod'] = hodify(q6['sparql'])

queries['vav triples'] = q6
varorder['vav triples'] = ['?pred','?obj']

#### QUERY 7
q7 = {}
q7['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?x WHERE {
    ?x rdf:type brick:Room .
}
""".strip()
q7['hod'] = hodify(q7['sparql'])
queries['q7'] = q7
varorder['q7'] = ['?x']

#### QUERY 8
q8 = {}
q8['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?x WHERE {
    ?ahu rdf:type brick:AHU .
    ?ahu bf:feeds ?x .
}
""".strip()
q8['hod'] = hodify(q8['sparql'])
queries['q8'] = q8
varorder['q8'] = ['?x']

#### QUERY 9
q9 = {}
q9['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?x WHERE {
    ?ahu rdf:type brick:AHU .
    ?ahu bf:feeds+ ?x .
}
""".strip()
q9['hod'] = hodify(q9['sparql'])
queries['q9'] = q9
varorder['q9'] = ['?x']

#### QUERY 10
q10 = {}
q10['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?x WHERE {
    ?ahu rdf:type brick:AHU .
    ?x bf:isFedBy+ ?ahu .
}
""".strip()
q10['hod'] = hodify(q10['sparql'])
queries['q10'] = q10
varorder['q10'] = ['?x']

#### QUERY 11
q11 = {}
q11['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?x WHERE {
    ?ahu rdf:type brick:AHU .
    ?ahu bf:feeds/bf:feeds ?x .
}
""".strip()
q11['hod'] = hodify(q11['sparql'])
queries['q11'] = q11
varorder['q11'] = ['?x']

#### QUERY 12
q12 = {}
q12['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?x WHERE {
    ?ahu rdf:type brick:AHU .
    ?ahu bf:feeds/bf:feeds+ ?x .
}
""".strip()
q12['hod'] = hodify(q12['sparql'])
queries['q12'] = q12
varorder['q12'] = ['?x']

#### QUERY 13
q13 = {}
q13['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?x WHERE {
    ?ahu rdf:type brick:AHU .
    ?ahu bf:feeds/bf:feeds? ?x .
}
""".strip()
q13['hod'] = hodify(q13['sparql'])
queries['q13'] = q13
varorder['q13'] = ['?x']

#### QUERY 14
q14 = {}
q14['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?x WHERE {
    ?ahu rdf:type brick:AHU .
    ?x bf:isFedBy/bf:isFedBy? ?ahu .
}
""".strip()
q14['hod'] = hodify(q14['sparql'])
queries['q14'] = q14
varorder['q14'] = ['?x']

#### QUERY 15
q15 = {}
q15['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?x WHERE {
    ?ahu rdf:type brick:AHU .
    ?ahu bf:feeds* ?x .
}
""".strip()
q15['hod'] = hodify(q15['sparql'])
queries['q15'] = q15
varorder['q15'] = ['?x']

#### QUERY 16
q16 = {}
q16['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?x WHERE {
    ?ahu rdf:type brick:AHU .
    ?x bf:isFedBy* ?ahu .
}
""".strip()
q16['hod'] = hodify(q16['sparql'])
queries['q16'] = q16
varorder['q16'] = ['?x']

#### QUERY 17
q17 = {}
q17['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?vav ?room WHERE {
    ?vav rdf:type brick:VAV .
    ?room rdf:type brick:Room .
    ?zone rdf:type brick:HVAC_Zone .
    ?vav bf:feeds+ ?zone .
    ?room bf:isPartOf ?zone .
}
""".strip()
q17['hod'] = hodify(q17['sparql'])
queries['q17'] = q17
varorder['q17'] = ['?vav','?room']

#### QUERY 18
q18 = {}
q18['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?sensor WHERE {
    ?sensor rdf:type/rdfs:subClassOf* brick:Zone_Temperature_Sensor .
}
""".strip()
q18['hod'] = hodify(q18['sparql'])
queries['q18'] = q18
varorder['q18'] = ['?sensor']

#### QUERY 19
q19 = {}
q19['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?sensor ?room WHERE {
    ?sensor rdf:type/rdfs:subClassOf* brick:Zone_Temperature_Sensor .
    ?room rdf:type brick:Room .
    ?vav rdf:type brick:VAV .
    ?zone rdf:type brick:HVAC_Zone .
    ?vav bf:feeds+ ?zone .
    ?zone bf:hasPart ?room .
    ?sensor bf:isPointOf ?vav .
}
""".strip()
q19['hod'] = hodify(q19['sparql'])
queries['q19'] = q19
varorder['q19'] = ['?sensor','?room']

#### QUERY 20
q20 = {}
q20['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?sensor ?room WHERE {
 ?sensor rdf:type/rdfs:subClassOf* brick:Zone_Temperature_Sensor .
 ?vav rdf:type brick:VAV .
 ?zone rdf:type brick:HVAC_Zone .
 ?room rdf:type brick:Room .
 ?vav bf:feeds+ ?zone .
 ?zone bf:hasPart ?room .
 {
    { ?sensor bf:isPointOf ?vav  }
    UNION
    { ?sensor bf:isPointOf ?room  }
 }
}
""".strip()
q20['hod'] = """
SELECT ?sensor ?room WHERE {
 ?sensor rdf:type/rdfs:subClassOf* brick:Zone_Temperature_Sensor .
 ?vav rdf:type brick:VAV  .
 ?zone rdf:type brick:HVAC_Zone  .
 ?room rdf:type brick:Room  .
 ?vav bf:feeds+ ?zone  .
 ?zone bf:hasPart ?room  .
 {
    { ?sensor bf:isPointOf ?vav .}
    OR
    { ?sensor bf:isPointOf ?room .}
 }
};
"""
queries['q20'] = q20
varorder['q20'] = ['?sensor','?room']

#### QUERY 21
q21 = {}
q21['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?sensor ?room WHERE {
    ?sensor rdf:type/rdfs:subClassOf* brick:Zone_Temperature_Sensor .
    ?room rdf:type brick:Room .
    ?vav rdf:type brick:VAV .
    ?zone rdf:type brick:HVAC_Zone .
    ?vav bf:feeds+ ?zone .
    ?zone bf:hasPart ?room .
    ?sensor bf:isPointOf ?room .
}
""".strip()
q21['hod'] = hodify(q21['sparql'])
queries['q21'] = q21
varorder['q21'] = ['?sensor','?room']

#### QUERY 22
q22 = {}
q22['sparql'] = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT ?vav ?x ?y WHERE {
    ?vav rdf:type brick:VAV .
    ?vav bf:hasPoint ?x .
    ?vav bf:isFedBy ?y .
}
""".strip()
q22['hod'] = hodify(q22['sparql'])
queries['q22'] = q22
varorder['q22'] = ['?vav','?x','?y']
