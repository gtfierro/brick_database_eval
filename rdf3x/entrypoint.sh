#!/bin/bash

cd gh-rdf3x
bin/rdf3xload berkeley /berkeley.ttl
./proxy
