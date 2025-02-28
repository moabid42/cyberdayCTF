FROM ubuntu:22.04 AS base

FROM pwn.red/jail
COPY --from=base / /srv

COPY l3ak /srv/app/run
RUN chmod +x /srv/app/run

ENV JAIL_TIME=180 JAIL_CPU=100 JAIL_MEM=10M
