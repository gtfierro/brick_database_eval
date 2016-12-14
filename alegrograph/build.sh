cp ../Brick.ttl .
cp ../BrickFrame.ttl .
cp ../berkeley.ttl .
docker build -t gtfierro/alegrograph .
docker push gtfierro/alegrograph
rm *.ttl
