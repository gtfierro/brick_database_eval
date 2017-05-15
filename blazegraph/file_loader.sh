sleep 20
echo "Loading"
curl -D- -H 'Content-Type: text/turtle' --upload-file /data/Brick.ttl -X POST 'http://localhost:9998/blazegraph/sparql'
curl -D- -H 'Content-Type: text/turtle' --upload-file /data/berkeley.ttl -X POST 'http://localhost:9998/blazegraph/sparql'
curl -D- -H 'Content-Type: text/turtle' --upload-file /data/BrickFrame.ttl -X POST 'http://localhost:9998/blazegraph/sparql'
echo "Loaded"
