wrk.method = "POST"
wrk.body   = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> PREFIX brick: <http://buildsys.org/ontologies/Brick#> PREFIX bf: <http://buildsys.org/ontologies/BrickFrame#> SELECT ?vav WHERE {     ?vav rdf:type brick:VAV . };"
wrk.headers["Content-Type"] = "application/json"
