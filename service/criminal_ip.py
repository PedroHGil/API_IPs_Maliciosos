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
        try:
            return{
                "Criminal IP": {
                    "whois": response['whois']                  if response.get('whois') else "Sem dados relacionado a essa URL",
                    "vulnerability": response['vulnerability']  if response.get('vulnerability') else "Sem dados relacionado a essa URL",
                }
            }
        except:
            return{
                "Criminal IP": {
                    "msg": "Sem dados relacionado a essa URL"
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
        
        try:
            return{
                "Criminal IP": {
                    "Score": response['data']['reports'][00]['score']       if response['data'].get('reports') else "Sem dados realcionado a essa URL",
                    "id": response['data']['reports'][00]['scan_id']        if response['data'].get('reports') else "Sem dados realcionado a essa URL",
                    "Problemas": response['data']['reports'][00]['issue']   if response['data'].get('reports') else "Sem dados realcionado a essa URL"
                }
            }
            
        except:
             return{
                "Criminal IP": {
                    "msg": "Sem dados relacionado a essa URL"
                }
            }
            
    
        

        