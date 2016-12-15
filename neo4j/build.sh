cp ../Brick.ttl .
cp ../BrickFrame.ttl .
cp ../berkeley.ttl .
docker build -t gtfierro/neo4jsparql .
docker push gtfierro/neo4jsparql
rm *.ttl
