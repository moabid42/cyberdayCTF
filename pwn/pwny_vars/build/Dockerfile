FROM ubuntu:20.04

RUN apt-get update && apt-get install -y socat gcc python
RUN rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/pwn
WORKDIR /usr/src/pwn
RUN cd /usr/src/pwn/

COPY flag.txt ./
RUN chmod 444 flag.txt
RUN adduser pwn

COPY pwny.c ./
RUN gcc -o pwny pwny.c
RUN chmod 111 pwny
RUN rm pwny.c
USER pwn

CMD socat -T60 TCP-LISTEN:2222,fork,reuseaddr EXEC:"./pwny"
