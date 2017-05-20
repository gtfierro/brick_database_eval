cp ../Brick.ttl .
cp ../BrickFrame.ttl .
cp ../berkeley.ttl .
cp `which hod` .
docker build -t gtfierro/hod .
docker push gtfierro/hod
