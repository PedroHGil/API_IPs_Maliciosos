import requests
import json

def get_virus(virus):
       
    url = 'https://www.virustotal.com/api/v3/ip_addresses/{}'.format(virus.ip)

    headers = {'X-Apikey':'55bd2bde973ef6420070bddfa8727eb2c4ed977bd6870492856f62cc6835578c'}
    
    response = json.loads(requests.get(url, headers=headers).text)
    
    return{
           "Reports por anti-virus": response['data']['attributes']['last_analysis_stats']
           }