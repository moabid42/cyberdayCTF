FROM ubuntu:20.04

RUN apt-get update && apt-get install -y socat gcc python
RUN rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/pwn
WORKDIR /usr/src/pwn
RUN cd /usr/src/pwn/

RUN adduser pwn
COPY l3ak.c ./
RUN gcc -o l3ak l3ak.c
RUN chmod 111 l3ak
RUN rm l3ak.c
USER pwn

CMD socat -T60 TCP-LISTEN:9999,fork,reuseaddr EXEC:"./l3ak"
