import requests
import json
from service.utils import credenciais
from service.utils import URLS

class CriminalIP_API:      
    def get_report(ip):
        
        api_url = URLS
        api_key = credenciais
        
        URL = api_url.GetURL.URL_CRIMINAL_IP

        headers = {
            "x-api-key": api_key.Credenciais.API_3
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
        
        
    def get_report_url(criminal):
         
        api_url = URLS
        api_key = credenciais
        
        headers = {
            "x-api-key": api_key.Credenciais.API_3
        }
        
        params = {
            "query": criminal,
            "offset": 0
            
        }
        URL = api_url.GetURL.URL_CRIMINAL_IP_URL

        response = json.loads(requests.get(url=URL, params=params, headers=headers).content)

        return{
            "Criminal IP": {
                "Score": response['data']['reports'][00]['score'],
                "id": response['data']['reports'][00]['scan_id'],
                "issues": response['data']['reports'][00]['issue']
            }
        }
    
    
        

        