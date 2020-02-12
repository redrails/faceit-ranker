import json
import pycurl
from io import BytesIO 
import pandas as pd

api_key = "1a9dda82-0083-4f90-9eae-9971e02b9a7e"
hub_id = "011b67b8-7622-4fd1-8d9c-e20e42ea6f3d"

b_obj = BytesIO() 
crl = pycurl.Curl() 

# Hard coded curl request for now
crl.setopt(crl.URL,"https://open.faceit.com/data/v4/hubs/"+hub_id+"/matches?offset=1&limit=1")
crl.setopt(crl.SSL_VERIFYHOST, 0)

crl.setopt(crl.SSL_VERIFYPEER, 0)
header = ['Authorization: Bearer '+api_key]

crl.setopt(crl.HTTPHEADER, header)
crl.setopt(crl.WRITEDATA, b_obj)
crl.perform()
crl.close()

get_body = b_obj.getvalue()

data = json.loads(get_body)
last_match_id = data["items"][0]["match_id"]