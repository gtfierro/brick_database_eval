FROM ubuntu:xenial
MAINTAINER Jason Koh <jbkoh@eng.ucsd.edu>

RUN apt-get update && apt-get install -y curl git openjdk-8-jdk
RUN sysctl -w vm.swappiness=0
COPY blazegraph.jar .
#COPY RWStore.properties /opt/
COPY fullfeature.properties /opt/
#RUN java -server -Xmx4g -jar blazegraph.jar
ADD entrypoint.sh /bin/ 
ADD file_loader.sh /bin/ 

RUN mkdir /data/

COPY berkeley.ttl /data/
COPY Brick.ttl /data/
COPY BrickFrame.ttl /data/

ENTRYPOINT ["/bin/entrypoint.sh"]

EXPOSE 9998
