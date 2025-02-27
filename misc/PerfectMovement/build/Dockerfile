FROM python:alpine

# Install socat to run the challenge through it:
RUN apk add --no-cache socat

# Setup a ctf user
RUN addgroup -S ctf && adduser -S -g ctf ctf

# Set the working directory to /home/ctf
WORKDIR /home/ctf

# Copy relevant files into the docker container:
COPY server.py solver.py common.py ./

# Give the ctf user permissions to relevant directories
RUN chmod -R 444 server.py solver.py common.py
RUN chown -R ctf:ctf /home/ctf

# Change to the ctf-user context
USER ctf

# Run the challenge through socat:
# Options:
# '-T 30': Terminate stale connections 30 seconds after the last transmission.
# 'TCP-LISTEN:8448': Pipe the programs IO through 8448/tcp
# 'nodelay': Turns off the Nagle algorithm for measuring the RTT (round trip time).
# 'reuseaddr': Allows multiple clients to bind to the local port used by socat.
# 'fork': Forks a child-process to run the application in.
# 'EXEC:"python /app/server.py"' Run 'python /app/server.py', if a client connects.
CMD socat -T 30 TCP-LISTEN:8447,nodelay,reuseaddr,fork EXEC:"python /home/ctf/server.py"

# Declare the required port
EXPOSE 8447/tcp
