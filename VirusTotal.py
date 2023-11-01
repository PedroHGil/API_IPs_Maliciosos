import requests
import json

url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'

def get_virus(virus):
    params = {
    'apikey':'55bd2bde973ef6420070bddfa8727eb2c4ed977bd6870492856f62cc6835578c',
    'ip':virus.ip
    }
    response = json.loads(requests.get(url, params=params).text)
    return{"Reports por anti-virus": response['undetected_urls'][0][2],
           "Total de anti-virus": response['undetected_urls'][0][3]
    }