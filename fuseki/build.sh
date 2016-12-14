cp ../Brick.ttl .
cp ../BrickFrame.ttl .
cp ../berkeley.ttl .
docker build -t gtfierro/fuseki .
docker push gtfierro/fuseki
