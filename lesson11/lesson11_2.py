import requests
from requests import Response
from pprint import pprint

url:str = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?page=0&size=100'
response:requests.Response = requests.get(url,timeout=5)
if response.status_code == 200:
    print("下載成功")
else:
    print("下載失敗")

pprint(response.text,compact=True,width=300,depth=True)