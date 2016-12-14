set -x
docker pull gtfierro/fuseki
docker kill fuseki
docker rm fuseki
docker run -d --name fuseki -p3031:3030 gtfierro/fuseki
