cp ../Brick.ttl .
cp ../BrickFrame.ttl .
cp ../berkeley.ttl .
docker build -t gtfierro/hod .
docker push gtfierro/hod
