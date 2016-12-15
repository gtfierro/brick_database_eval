set -x
docker pull gtfierro/rdf3x
docker kill rdf3x
docker rm rdf3x
docker run -d --name rdf3x -p8080:8080 gtfierro/rdf3x
