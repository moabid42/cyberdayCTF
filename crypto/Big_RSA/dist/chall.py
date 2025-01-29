from Crypto.Util.number import *

p=getPrime(2048)
q=getPrime(2048)
N=p*q

phi=(p-1) * (q-1)

while 1 :
    d = getPrime(512)
    e=inverse(d,phi)
    if len(bin(e)[2:]) == len(bin(e)[2:]):
        print(f"N = {N}\ne={e}")
        break

FLAG=bytes_to_long(b"42HN{REDACTED}")
ciphertext=pow(FLAG,e,N)
print(f"ciphertext = {ciphertext}")