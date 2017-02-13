#!/bin/bash

bash /bin/file_loader.sh &

java -server -Xmx4g -Djetty.port=9998 -jar blazegraph.jar /opt/fullfeature.properties

#curl -D- -H 'Content-Type: text/turtle' --upload-file /data/Brick.ttl -X POST 'http://localhost:9999/blazegraph/sparql'
#curl -D- -H 'Content-Type: text/turtle' --upload-file /data/Berkeley.ttl -X POST 'http://localhost:9999/blazegraph/sparql'
#curl -D- -H 'Content-Type: text/turtle' --upload-file /data/BrickFrame.ttl -X POST 'http://localhost:9999/blazegraph/sparql'
