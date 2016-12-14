FROM ubuntu:xenial
MAINTAINER Gabe Fierro <gtfierro@eecs.berkeley.edu>

RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:ubuntu-lxc/lxd-stable
RUN apt-get update
RUN apt-get install -y golang git libraptor2-dev
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /go
ENV GOPATH /go
RUN go get -u github.com/gtfierro/hod 
RUN go install github.com/gtfierro/hod 

ADD entrypoint.sh /bin/
ADD hodconfig.yaml Brick.ttl BrickFrame.ttl berkeley.ttl /

ENTRYPOINT [ "/bin/entrypoint.sh" ]
