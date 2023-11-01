import requests
import json

URL = "https://otx.alienvault.com/api/v1/indicators/submit_url"

params = {'url':'118.25.6.39','tlp':1, 'X-OTX-API-KEY':'c282ce1a7bc2925e9ac187a28171f3e257cd61304ce54ff20e0684227704a9e7'}
response = requests.get(URL, params=params)
print(response.json())