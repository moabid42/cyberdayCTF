#!/bin/bash

docker build -t geosint-main .
docker run -p 4003:6958 -d geosint-main

