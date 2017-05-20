#!/bin/bash

cd /
/bin/hod load -c /hodconfig.yaml berkeley.ttl
/bin/hod http -c /hodconfig.yaml
