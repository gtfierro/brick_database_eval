wrk.method = "POST"
wrk.body   = "SELECT ?vav ?room WHERE { ?vav rdf:type brick:VAV . ?room rdf:type brick:Room . ?zone rdf:type brick:HVAC_Zone . ?vav bf:feeds+ ?zone . ?room bf:isPartOf ?zone . };"
wrk.headers["Content-Type"] = "application/json"
