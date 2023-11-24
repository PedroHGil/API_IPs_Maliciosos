import requests
import json
from service.utils import credenciais
from service.utils import URLS

class AbuseIP_API:
      
    def __init__(self):
        self.api_url = URLS
        self.api_key = credenciais 
    
    def get_report(self, body):   
        
        url = self.api_url.GetURL.URL_ABUSE_IP

        headers = {
             'Accept': 'application/json',
             'Key': self.api_key.Credenciais.API_1
         }
        
        querystring = {
         'ipAddress': body,
         'maxAgeInDays': '90'
         }
        
        response = json.loads(requests.get(url=url, headers=headers, params=querystring).text)
        
        try:
                      
            return {
                       "Abuse IP": {
                            "malicioso": response['data']['abuseConfidenceScore'] if response['data'].get('abuseConfidenceScore') else "Sem dados relacionado a esse IP",
                            "ip": response['data']['ipAddress']                   if response['data'].get('ipAddress') else "Sem dados relacionado a esse IP",
                            "Dominio": response['data']['domain']                 if response['data'].get('domain') else "Sem dados relacionado a esse IP",
                            "País": response['data']['countryCode']               if response['data'].get('countryCode') else "Sem dados relacionado a esse IP",
                            "Tipo": response['data']['usageType']                 if response['data'].get('usageType') else "Sem dados relacionado a esse IP"
                        }
                    } 
        except:
             return{
                "Abuse IP": {
                    "msg": "Sem dados relacionado a esse IP"
                }
            }