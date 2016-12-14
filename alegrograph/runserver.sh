set -x
docker pull gtfierro/alegrograph
docker kill alegrograph
docker rm alegrograph
docker run -d --name alegrograph -p10035:10035 gtfierro/alegrograph
