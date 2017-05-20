FROM ubuntu:xenial
MAINTAINER Gabe Fierro <gtfierro@eecs.berkeley.edu>

RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:ubuntu-lxc/lxd-stable
RUN apt-get update
RUN apt-get install -y git libraptor2-dev libssl-dev
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD go1.8.1.linux-amd64.tar.gz /usr/local

ADD hod /bin/hod
RUN mkdir /go
ENV GOPATH /go
RUN /usr/local/go/bin/go get github.com/gtfierro/hod
RUN /usr/local/go/bin/go install github.com/gtfierro/hod

ADD entrypoint.sh /bin/
ADD Brick.ttl hodconfig.yaml BrickFrame.ttl berkeley.ttl /

ENTRYPOINT [ "/bin/entrypoint.sh" ]
