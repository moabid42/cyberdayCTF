FROM ubuntu:20.04

RUN apt-get update && apt-get install -y socat gcc python
RUN rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/pwn
WORKDIR /usr/src/pwn
RUN cd /usr/src/pwn/

COPY flag.txt ./
RUN chmod 444 flag.txt
RUN adduser pwn
COPY shell.c ./
RUN gcc -std=c99 -o shell shell.c -O0 -fno-stack-protector -z execstack -no-pie -g -Wno-deprecated-declarations
RUN chmod 111 shell
RUN rm shell.c
USER pwn

CMD socat -T60 TCP-LISTEN:2000,fork,reuseaddr EXEC:"./shell"
