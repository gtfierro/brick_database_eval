wget https://github.com/blazegraph/database/releases/download/BLAZEGRAPH_RELEASE_2_1_4/blazegraph.jar
cp ../Brick.ttl .
cp ../BrickFrame.ttl .
cp ../berkeley.ttl .
docker build -t jbkoh/blazegraph .
docker push jbkoh/blazegraph
