benchqueries = {}

sparql = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
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

sparql = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
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

sparql = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
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

sparql = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
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

sparql = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT DISTINCT ?sensor ?room
WHERE {
    { ?sensor rdf:type/rdfs:subClassOf* brick:Zone_Temperature_Sensor . }
    UNION
    { ?sensor rdf:type/rdfs:subClassOf* brick:Discharge_Air_Temperature_Sensor . }
    UNION
    { ?sensor rdf:type/rdfs:subClassOf* brick:Occupancy_Sensor . }
    UNION
    { ?sensor rdf:type/rdfs:subClassOf* brick:CO2_Sensor . }
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

sparql = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT DISTINCT ?vav ?pred ?obj WHERE {
    ?vav rdf:type brick:VAV .
    ?vav ?pred ?obj .
}
"""
hod = """
SELECT ?vav ?pred ?obj WHERE {
    ?vav rdf:type brick:VAV .
    ?vav ?pred ?obj .
};
"""
benchqueries['VAVRelships'] = {'sparql': sparql, 'hod': hod}

sparql = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX brick: <http://buildsys.org/ontologies/Brick#>
PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#>
SELECT DISTINCT ?vav ?room ?temp_uuid ?valve_uuid ?damper_uuid ?setpoint_uuid WHERE {
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
