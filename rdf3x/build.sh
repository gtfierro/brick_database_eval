cp ../Brick.ttl .
cp ../BrickFrame.ttl .
cp ../berkeley.ttl .
go build -o proxy
sed -i -e 's/_//g' berkeley.ttl
docker build -t gtfierro/rdf3x .
docker push gtfierro/rdf3x
rm *.ttl
