import requests
import json
from service.utils import credenciais
from service.utils import URLS

class CriminalIP_API:   
    
    def __init__(self):
        self.api_url = URLS
        self.api_key = credenciais 
           
    def get_report(self, ip):
        
        URL = self.api_url.GetURL.URL_CRIMINAL_IP

        headers = {
            "x-api-key": self.api_key.Credenciais.API_3
        }
        
        params = {
            "ip": ip,
            "full": False
        }

        response = json.loads(requests.get(url=URL, params=params, headers=headers).content)

        return{
            "Criminal IP": {
                "whois": response['whois'],
                "vulnerability": response['vulnerability']
            }
        }
        
        
    def get_report_url(self, criminal):
         
        
        headers = {
            "x-api-key": self.api_key.Credenciais.API_3
        }
        
        params = {
            "query": criminal,
            "offset": 0
            
        }
        URL = self.api_url.GetURL.URL_CRIMINAL_IP_URL

        response = json.loads(requests.get(url=URL, params=params, headers=headers).content)

        return{
            "Criminal IP": {
                "Score": response['data']['reports'][00]['score'] if len(response['data']['reports']) > 1 else "Sem dados realcionado a essa URL",
                "id": response['data']['reports'][00]['scan_id'] if len(response['data']['reports']) > 1 else "Sem dados realcionado a essa URL",
                "issues": response['data']['reports'][00]['issue'] if len(response['data']['reports']) > 1 else "Sem dados realcionado a essa URL"
            }
        }
    
    
        

        