import requests
import json
from service.utils import credenciais
from service.utils import URLS


class VirusTotal_API:
    
    
    def __init__(self):
        self.api_url = URLS
        self.api_key = credenciais 
      
    
    def get_report_ip(self, ip):
        
        url = self.api_url.GetURL.URL_VIRUS_TOTAL_IP.format(ip)

        headers = {'X-Apikey': self.api_key.Credenciais.API_2}

        response = json.loads(requests.get(url, headers=headers).text)

        try:
            
            return{
                "Virus Total": {
                    "Reports por anti-virus": response['data']['attributes']['last_analysis_stats']
                    }
                }
        except:
             return{
                "Virus Total": {
                    "msg": "Sem dados relacionado a esse IP"
                }
            }
        
    def get_report_url(self, url):
        
        url = self.api_url.GetURL.URL_VIRUS_TOTAL_URL.format(url)

        headers = {'X-Apikey': self.api_key.Credenciais.API_2}

        response = json.loads(requests.get(url, headers=headers).text)

        try:
            return{
                "Virus Total": {
                    "Reports por anti-virus": response['data']['attributes']['last_analysis_stats']
                    }
                }
        except:
             return{
                "Virus Total": {
                    "msg": "Sem dados relacionado a essa URL"
                }
            }