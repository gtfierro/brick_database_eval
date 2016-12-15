FROM ubuntu:xenial
MAINTAINER Gabe Fierro <gtfierro@eecs.berkeley.edu>

RUN apt-get update && apt-get install -y git python python-dev python-pip && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install flask rdflib
ADD app.py /

ADD Brick.ttl BrickFrame.ttl berkeley.ttl /
ADD entrypoint.sh /bin/

ENTRYPOINT [ "/bin/entrypoint.sh" ]
