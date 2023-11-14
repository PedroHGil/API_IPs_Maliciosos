import requests
import json
from service.utils import credenciais
from service.utils import URLS

class AbuseIP_API:
    
    def get_report(body):   
        
        api_url = URLS
        api_key = credenciais
        
        url = api_url.GetURL.URL_ABUSE_IP

        headers = {
             'Accept': 'application/json',
             'Key': api_key.Credenciais.API_1
         }
        
        querystring = {
         'ipAddress': body,
         'maxAgeInDays': '90'
         }
        
        response = json.loads(requests.get(url=url, headers=headers, params=querystring).text)
        
        return {
                   "Abuse IP": {
                        "malicioso": response['data']['abuseConfidenceScore'],
                        "ip": response['data']['ipAddress'],
                        "Dominio": response['data']['domain'],
                        "País": response['data']['countryCode'],
                        "Tipo": response['data']['usageType']
                    }
                } 