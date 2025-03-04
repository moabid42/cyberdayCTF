FROM python:3-slim
RUN apt-get update -y && apt-get dist-upgrade -y && apt-get install socat gcc -y
COPY ./flag.txt /app/flag.txt
COPY ./chall.py /app/chall.py

CMD ["socat", "TCP-LISTEN:3333,reuseaddr,fork", "EXEC:\"python /app/chall.py\",stderr"]
