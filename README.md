# Brick Database Eval


DBs to evaluate:
- [Jena/Fuseki](https://jena.apache.org/documentation/serving_data/):
    - also need to experiment w/ different ordering of clauses in SPARQL query
- [neo4j/sparql](https://github.com/neo4j-contrib/sparql-plugin):
    - blog w/ basic directions: http://www.snee.com/bobdc.blog/2014/01/storing-and-querying-rdf-in-ne.html
- [alegrograph](http://franz.com/agraph/downloads/)
    - has free download!
- [rdf3x](https://github.com/gh-rdf3x/gh-rdf3x)
- [python rdflib](https://rdflib.readthedocs.io/en/stable/)
- [top braid](http://www.topquadrant.com/products/topbraid-live/)
    - expensive!
- Cayley/gremlin:
    - supposedly full Gremlin query lang can translate btwn SPARQL,
      but the subset currently implemented in Cayley cannot


### Process

- have a family of queries we want to run:
    - start with the 8 application queries for the Brick paper!
- need to "rewrite" the query for each database:
    - HodDB and rdf3x may need some tweaking
- 10 runs; take the average

- for each database, we have a directory containing:
    - Dockerfile for running the server
    - instructions for how to execute a query
    - code for running the queries

- which file do we run this on?
    - start with `berkeley.ttl`/`soda_brick.ttl`

### Literature

- NOSQL database for RDF: an empirical evaluation
    - website: http://ribs.csres.utexas.edu/nosqlrdf/

