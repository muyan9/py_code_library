from suds import WebFault
from suds.client import Client
import time

url = 'http://120.27.42.162:8080/t?WSDL'
client = Client(url)

t1 = time.time()
for i in range(3):
    client.service.log("did", int(1433814727.8627*1000), "msg")
print time.time() - t1