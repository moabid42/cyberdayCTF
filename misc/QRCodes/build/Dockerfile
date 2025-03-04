# Use an alpine python image as the base image:
FROM python:3.13-slim

# Install socat to run the challenge through it:
RUN apt-get update && apt-get install -y socat libzbar0 ffmpeg libsm6 libxext6 && rm -rf /var/lib/apt/lists/*

# Setup a ctf user
RUN groupadd -r ctf && useradd -r -g ctf ctf

# Set the working directory to /home/ctf
WORKDIR /home/ctf

# Copy relevant files into the docker container:
COPY server.py hidden.py ./

# Give the ctf user permissions to relevant directories
RUN chmod -R 444 server.py hidden.py
RUN chown -R ctf:ctf /home/ctf

# Change to the ctf-user context
USER ctf

# Add the required python modules (-> using the ctf-user, because pip warns about issues when running as root...):
RUN pip install --no-cache-dir pyzbar PyQRCode pypng opencv-python

# Run the challenge through socat:
# Options:
# '-T 30': Terminate stale connections 30 seconds after the last transmission.
# 'TCP-LISTEN:8448': Pipe the programs IO through 8448/tcp
# 'nodelay': Turns off the Nagle algorithm for measuring the RTT (round trip time).
# 'reuseaddr': Allows multiple clients to bind to the local port used by socat.
# 'fork': Forks a child-process to run the application in.
# 'EXEC:"python /app/server.py"' Run 'python /app/server.py', if a client connects.
CMD socat -T 30 TCP-LISTEN:8448,nodelay,reuseaddr,fork EXEC:"python /home/ctf/server.py"

# Declare the required port
EXPOSE 8448/tcp
    