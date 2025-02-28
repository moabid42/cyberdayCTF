from Crypto.Util.number import *
flag=b"42HN{fake_flag}"
p = getPrime(512)
q = getPrime(512)
n = p*q
e=0x10001
c=pow(bytes_to_long(flag),e,n)

l = p % 2**420
print(f"n={n}\nc={c}\ne={e}\nl={l}")
