FROM ubuntu:xenial
MAINTAINER Gabe Fierro <gtfierro@eecs.berkeley.edu>

RUN apt-get update && apt-get install -y curl git

ADD agraph-6.1.3-linuxamd64.64.tar.gz .
RUN cd agraph-6.1.3 ; ./install-agraph --no-configure --supersede /opt/agraph
RUN cd agraph-6.1.3 ; ./configure-agraph --config-file /opt/agraph/lib/agraph.cfg --data-dir /opt/agraph/data --log-dir /opt/agraph/log --pid-file /opt/agraph/data/agraph.pid --port 10035 --runas-user root --super-user root --super-password asdfasdf --instance-timeout 604800 --non-interactive

ADD berkeley.ttl .
ADD Brick.ttl .
ADD BrickFrame.ttl .
ADD entrypoint.sh /bin/

ENTRYPOINT ["/bin/entrypoint.sh"]
