FROM python:slim AS app

FROM pwn.red/jail
COPY --from=app / /srv

COPY chall.py /srv/app/run
COPY words.txt /srv/app/words.txt
COPY flag.txt /srv/app/flag.txt

RUN chmod +x /srv/app/run

RUN mv /srv/app/flag.txt /srv/app/flag-$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 64 | head -n 1).txt

ENV JAIL_PIDS=40 JAIL_TIME=60 JAIL_MEM=60M 
