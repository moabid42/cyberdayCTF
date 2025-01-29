from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

Encrypted1  = "2545af71e22c1f97ca864a6680c7edb60eccd0797449bce51331e3a122a4dfdc"
IV1 = "a35a38d6f3816c69e5f1ea961f500247"
Encrypted2  = "e3b8df3d5b7375deba89505f726658b01679586c3150420e7673672c373c6f318c96cd9f222136519ca0c0cff726f03cdd68e9ff5a4cabe263d2687349ffadefeaefbc2cc5179fbd059b9d32acacdca88a1ba09548b0a1667aeb1f7010fa26191837b763e8ff53219caad4e9456a73bb631b81cd136a6b921e8c5fea94f2d1f0fd9cdfbf20ed986a9c83d4bf574b197d6a92a088616bfa43c5f9c0c63910de6f"
IV2 = "08712e11bd6baa47d706060584feec21"

enc1 = bytes.fromhex(Encrypted1) # flag_enc
enc2 = bytes.fromhex(Encrypted2) # lorem_enc
iv1 = bytes.fromhex(IV1)
iv2 = bytes.fromhex(IV2)

plain1 = b"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s."

# Recover the iv
cipher1 = AES.new(iv2, AES.MODE_CBC,plain1[:16]) 
iv = cipher1.decrypt(enc2[:16]) 
print(f"iv = {iv.hex()}")
# Decrypt the flag
cipher2=AES.new(iv1,AES.MODE_CBC,iv)
flag=unpad(cipher2.decrypt(enc1),16)
print(f"flag = {flag.decode()}")

