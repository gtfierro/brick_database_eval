FROM ubuntu:xenial
MAINTAINER Gabe Fierro <gtfierro@eecs.berkeley.edu>

RUN apt-get update && apt-get install -y curl git graphviz maven make openjdk-8-jdk devscripts debhelper rpm

RUN curl -O https://codeload.github.com/neo4j/neo4j/tar.gz/3.1.0
RUN tar xzf 3.1.0
RUN cd neo4j-3.1.0 ; mvn clean install -DskipTests
RUN cd neo4j-3.1.0/packaging/standalone/target ; tar xzf neo4j-community-3.1.0-SNAPSHOT-unix.tar.gz
RUN cd neo4j-3.1.0/packaging/standalone/target/neo4j-community-3.1.0-SNAPSHOT ; git clone https://github.com/neo4j-contrib/sparql-plugin
RUN cd neo4j-3.1.0/packaging/standalone/target/neo4j-community-3.1.0-SNAPSHOT ; sed -i -e 's/#dbms.connectors.default_listen_address=0.0.0.0/dbms.connectors.default_listen_address=0.0.0.0/' conf/neo4j.conf 
RUN cd neo4j-3.1.0/packaging/standalone/target/neo4j-community-3.1.0-SNAPSHOT ; sed -i -e 's/#dbms.security.auth_enabled=false/dbms.security.auth_enabled=false/' conf/neo4j.conf 

ADD berkeley.ttl .
ADD Brick.ttl .
ADD BrickFrame.ttl .
ADD entrypoint.sh /bin/

#ENTRYPOINT ["/bin/entrypoint.sh"]
ENTRYPOINT ["/bin/bash"]
