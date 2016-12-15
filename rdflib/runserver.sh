set -x
docker pull gtfierro/rdflib
docker kill rdflib
docker rm rdflib
docker run -d --name rdflib -p8081:8081 gtfierro/rdflib
