FROM ubuntu:xenial
MAINTAINER Gabe Fierro <gtfierro@eecs.berkeley.edu>

RUN apt-get update && apt-get install -y curl git default-jre default-jdk vim ruby-full

ADD apache-jena-3.1.0.tar.gz /opt/jena/
ADD apache-jena-fuseki-2.4.0.tar.gz /opt/fuseki/

ADD berkeley.ttl .
ADD Brick.ttl .
ADD BrickFrame.ttl .
ADD entrypoint.sh /bin/

EXPOSE 3030

ENV JENAROOT=/opt/jena
ENV PATH=$JENAROOT/bin:$PATH

ENTRYPOINT ["/bin/entrypoint.sh"]
