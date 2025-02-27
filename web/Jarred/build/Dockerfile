FROM python:3.8-slim

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN useradd -m ctfuser

WORKDIR /app

# Copy challenge files
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Move the flag to a protected location
RUN mv flag.txt /flag.txt && \
    chmod 444 /flag.txt && \
    chown root:root /flag.txt

# Drop privileges by switching to the non-root user
USER ctfuser

EXPOSE 3002

ENV FLASK_APP=app.py

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=3002"]
