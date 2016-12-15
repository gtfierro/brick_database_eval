set -x
docker pull gtfierro/neo4jsparql
docker kill neo4jsparql
docker rm neo4jsparql
docker run -d --name neo4jsparql -p7474:7474 -p7687:7687 gtfierro/neo4jsparql
