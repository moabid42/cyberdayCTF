FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y \
    socat \
    musl-dev \
    && rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --gecos '' lowprivuser

WORKDIR /app

COPY . /app

RUN chmod +x /app/serve.sh /app/chall.py && \
    chown -R lowprivuser:lowprivuser /app && \
    chmod -R u-w /app

USER lowprivuser

CMD ["./serve.sh"]
