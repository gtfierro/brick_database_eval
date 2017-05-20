#!/bin/bash
set -x
cd /opt/fuseki/apache-jena-fuseki-2.4.0
./fuseki start
# enable non-localhost
sed -i -e 's/\(.*localhostFilter\)/#\1/' run/shiro.ini
./fuseki stop
mkdir DB
./fuseki-server --loc=DB /berkeley & 
pid=$!
sleep 5
bin/s-put http://localhost:3030/berkeley/data default /Brick.ttl
bin/s-put http://localhost:3030/berkeley/data default /BrickFrame.ttl
bin/s-put http://localhost:3030/berkeley/data default /berkeley.ttl
kill $pid
sleep 1
./fuseki-server --loc=DB /berkeley
