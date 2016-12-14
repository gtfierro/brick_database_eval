#!/bin/bash

cd /opt/agraph
bin/agraph-control start
bin/agload berkeley /Brick.ttl
bin/agload berkeley /BrickFrame.ttl
bin/agload berkeley /berkeley.ttl
while true ; do sleep 100 ; done
