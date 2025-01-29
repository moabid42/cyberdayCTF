from Crypto.Cipher.AES import new, MODE_CBC
from Crypto.Util.Padding import pad
from os import urandom

flag = b"42HN{REDACTED}"
key = urandom(16)
iv1 = urandom(16)
cipher = new(iv1, MODE_CBC, key)
encrypted1 = cipher.encrypt(pad(flag, 16))

print(f"Encrypted1  = {encrypted1.hex()}")
print(f"IV1 = {iv1.hex()}")

plain1 = b"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s."
iv2 = urandom(16)
cipher = new(iv2, MODE_CBC, key)
encrypted2 = cipher.encrypt(pad(plain1, 16))

print(f"Encrypted2  = {encrypted2.hex()}")
print(f"IV2 = {iv2.hex()}")
