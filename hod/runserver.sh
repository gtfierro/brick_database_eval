set -x
docker pull gtfierro/paperhod
docker kill hod
docker rm hod
docker run -d --name hod -p47808:47808 gtfierro/paperhod
