cp ../Brick.ttl .
cp ../BrickFrame.ttl .
cp ../berkeley.ttl .
docker build -t gtfierro/rdflib .
docker push gtfierro/rdflib
rm *.ttl
