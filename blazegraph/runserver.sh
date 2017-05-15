set -x
docker pull gtfierro/blazegraph
docker kill blazegraph
docker rm blazegraph
docker run -d --name blazegraph -p9998:9998 gtfierro/blazegraph
