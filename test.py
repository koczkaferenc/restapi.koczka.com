# pip3 install http.client 
# Javítsd HTTPConnection-ra!

import http.client

conn = http.client.HTTPConnection("localhost", 5101)
payload = ''
headers = {}
conn.request("GET", "/hello?name=Anna", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))