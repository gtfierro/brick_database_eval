cp ../Brick.ttl .
cp ../BrickFrame.ttl .
cp ../berkeley.ttl berkeley.ttl
docker build -t gtfierro/paperhod .
docker push gtfierro/paperhod
