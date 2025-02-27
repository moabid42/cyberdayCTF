#!/bin/sh

socat \
-T60 \
TCP-LISTEN:2323,reuseaddr,fork \
EXEC:"timeout 180 python3 /app/chall.py"
