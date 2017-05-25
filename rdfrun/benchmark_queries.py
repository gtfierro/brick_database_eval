benchqueries = {}

sparql = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <https://brickschema.org/schema/1.0.1/Brick#>
PREFIX bf: <https://brickschema.org/schema/1.0.1/BrickFrame#>
SELECT DISTINCT ?vav WHERE {
    ?vav rdf:type brick:VAV .
}
"""
hod = """
SELECT ?vav WHERE {
    ?vav rdf:type brick:VAV .
};
"""
benchqueries['VAVEnum'] = {'sparql': sparql, 'hod': hod}
benchqueries['VAVEnum']['order'] = ['?vav']

sparql = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <https://brickschema.org/schema/1.0.1/Brick#>
PREFIX bf: <https://brickschema.org/schema/1.0.1/BrickFrame#>
SELECT DISTINCT ?sensor WHERE {
    ?sensor rdf:type/rdfs:subClassOf* brick:Zone_Temperature_Sensor .
}
"""
hod = """
SELECT ?sensor WHERE {
    ?sensor rdf:type/rdfs:subClassOf* brick:Zone_Temperature_Sensor .
};
"""
benchqueries['TempSensor'] = {'sparql': sparql, 'hod': hod}
benchqueries['TempSensor']['order'] = ['?sensor']

sparql = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <https://brickschema.org/schema/1.0.1/Brick#>
PREFIX bf: <https://brickschema.org/schema/1.0.1/BrickFrame#>
SELECT DISTINCT ?x WHERE {
    ?ahu rdf:type brick:AHU .
    ?ahu bf:feeds+ ?x .
}
"""
hod = """
SELECT ?x WHERE {
    ?ahu rdf:type brick:AHU .
    ?ahu bf:feeds+ ?x .
};
"""
benchqueries['AHUChildren'] = {'sparql': sparql, 'hod': hod}
benchqueries['AHUChildren']['order'] = ['?x']

sparql = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <https://brickschema.org/schema/1.0.1/Brick#>
PREFIX bf: <https://brickschema.org/schema/1.0.1/BrickFrame#>
SELECT DISTINCT ?floor ?room ?zone WHERE {
    ?floor rdf:type brick:Floor .
    ?room rdf:type brick:Room .
    ?zone rdf:type brick:HVAC_Zone .
    ?room bf:isPartOf+ ?floor .
    ?room bf:isPartOf+ ?zone .
}
"""
hod = """
SELECT ?floor ?room ?zone WHERE {
    ?floor rdf:type brick:Floor .
    ?room rdf:type brick:Room .
    ?zone rdf:type brick:HVAC_Zone .
    ?room bf:isPartOf+ ?floor .
    ?room bf:isPartOf+ ?zone .
};
"""
benchqueries['SpatialMapping'] = {'sparql': sparql, 'hod': hod}
benchqueries['SpatialMapping']['order'] = ['?floor','?room','?zone']

sparql = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <https://brickschema.org/schema/1.0.1/Brick#>
PREFIX bf: <https://brickschema.org/schema/1.0.1/BrickFrame#>
SELECT DISTINCT ?sensor ?room
WHERE {
    { ?sensor rdf:type/rdfs:subClassOf* brick:Zone_Temperature_Sensor }
    UNION
    { ?sensor rdf:type/rdfs:subClassOf* brick:Discharge_Air_Temperature_Sensor }
    UNION
    { ?sensor rdf:type/rdfs:subClassOf* brick:Occupancy_Sensor }
    UNION
    { ?sensor rdf:type/rdfs:subClassOf* brick:CO2_Sensor }
    ?vav rdf:type brick:VAV .
    ?zone rdf:type brick:HVAC_Zone .
    ?room rdf:type brick:Room .
    ?vav bf:feeds+ ?zone .
    ?zone bf:hasPart ?room .
    {?sensor bf:isPointOf ?vav }
    UNION
    {?sensor bf:isPointOf ?room }
}
"""
hod = """
SELECT ?sensor ?room
WHERE {
    {
        { ?sensor rdf:type/rdfs:subClassOf* brick:Zone_Temperature_Sensor . }
        UNION
        { ?sensor rdf:type/rdfs:subClassOf* brick:Discharge_Air_Temperature_Sensor . }
        UNION
        { ?sensor rdf:type/rdfs:subClassOf* brick:Occupancy_Sensor . }
        UNION
        { ?sensor rdf:type/rdfs:subClassOf* brick:CO2_Sensor . }
    }
    ?vav rdf:type brick:VAV .
    ?zone rdf:type brick:HVAC_Zone .
    ?room rdf:type brick:Room .
    ?vav bf:feeds+ ?zone .
    ?zone bf:hasPart ?room .
    {
        {?sensor bf:isPointOf ?vav }
        UNION
        {?sensor bf:isLocatedIn ?room }
    }
};
"""
benchqueries['SensorsInRooms'] = {'sparql': sparql, 'hod': hod}
benchqueries['SensorsInRooms']['order'] = ['?sensor','?room']

sparql = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <https://brickschema.org/schema/1.0.1/Brick#>
PREFIX bf: <https://brickschema.org/schema/1.0.1/BrickFrame#>
SELECT DISTINCT ?vav ?x ?y ?z ?a WHERE {
    ?vav rdf:type brick:VAV .
    ?vav bf:feeds+ ?x .
    ?vav bf:isFedBy+ ?y .
    ?vav bf:hasPoint+ ?z .
    ?vav bf:hasPart+ ?a .
}
"""
hod = """
SELECT ?vav ?x ?y ?z ?a WHERE {
    ?vav rdf:type brick:VAV .
    ?vav bf:feeds+ ?x .
    ?vav bf:isFedBy+ ?y .
    ?vav bf:hasPoint+ ?z .
    ?vav bf:hasPart+ ?a .
};
"""
benchqueries['VAVRelships'] = {'sparql': sparql, 'hod': hod}
benchqueries['VAVRelships']['order'] = ['?vav','?x','?y','?z','?a']

sparql = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <https://brickschema.org/schema/1.0.1/Brick#>
PREFIX bf: <https://brickschema.org/schema/1.0.1/BrickFrame#>
SELECT DISTINCT ?vav ?room ?temp_uuid ?valve_uuid ?setpoint_uuid WHERE {
    ?vav rdf:type brick:VAV .
    ?vav bf:hasPoint ?tempsensor .
    ?tempsensor rdf:type/rdfs:subClassOf* brick:Temperature_Sensor .
    ?tempsensor bf:uuid ?temp_uuid .
    ?vav bf:hasPoint ?valvesensor .
    ?valvesensor rdf:type/rdfs:subClassOf* brick:Valve_Command .
    ?valvesensor bf:uuid ?valve_uuid .
    ?vav bf:hasPoint ?setpoint .
    ?setpoint rdf:type/rdfs:subClassOf* brick:Zone_Temperature_Setpoint .
    ?setpoint bf:uuid ?setpoint_uuid .
    ?room rdf:type brick:Room .
    ?tempsensor bf:isLocatedIn ?room .
}
"""
hod = """
SELECT ?vav ?room ?temp_uuid ?valve_uuid ?setpoint_uuid WHERE {
    ?vav rdf:type brick:VAV .
    ?vav bf:hasPoint ?tempsensor .
    ?tempsensor rdf:type/rdfs:subClassOf* brick:Temperature_Sensor .
    ?tempsensor bf:uuid ?temp_uuid .
    ?vav bf:hasPoint ?valvesensor .
    ?valvesensor rdf:type/rdfs:subClassOf* brick:Valve_Command .
    ?valvesensor bf:uuid ?valve_uuid .
    ?vav bf:hasPoint ?setpoint .
    ?setpoint rdf:type/rdfs:subClassOf* brick:Zone_Temperature_Setpoint .
    ?setpoint bf:uuid ?setpoint_uuid .
    ?room rdf:type brick:Room .
    ?tempsensor bf:isLocatedIn ?room .
};
"""
benchqueries['GreyBox'] = {'sparql': sparql, 'hod': hod}
benchqueries['GreyBox']['order'] = ['?vav','?room','?temp_uuid','?valve_uuid','?setpoint_uuid']
