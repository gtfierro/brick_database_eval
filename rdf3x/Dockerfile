FROM ubuntu:xenial
MAINTAINER Gabe Fierro <gtfierro@eecs.berkeley.edu>

RUN apt-get update && apt-get install -y git build-essential && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN git clone https://github.com/gh-rdf3x/gh-rdf3x
RUN cd gh-rdf3x ; make

ADD Brick.ttl BrickFrame.ttl berkeley.ttl /
ADD proxy /gh-rdf3x
ADD entrypoint.sh /bin/

ENTRYPOINT [ "/bin/entrypoint.sh" ]
