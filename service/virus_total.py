import requests
import json
from utils import credenciais
from utils import urls


class VirusTotal_API:
    
    
    def get_report_ip(ip):
        
        api_url = urls
        api_key = credenciais
        
        url = api_url.URL.URL_VIRUS_TOTAL_IP.format(ip)

        headers = {'X-Apikey': api_key.Credenciais.API_2}

        response = json.loads(requests.get(url, headers=headers).text)

        return{
            "Virus Total": {
                "Reports por anti-virus": response['data']['attributes']['last_analysis_stats']
                }
            }
        
    def get_report_url(url):
        
        api_url = urls
        api_key = credenciais
        
        url = api_url.URL.URL_VIRUS_TOTAL_URL.format(url)

        headers = {'X-Apikey': api_key.Credenciais.API_2}

        response = json.loads(requests.get(url, headers=headers).text)

        return{
            "Virus Total": {
                "Reports por anti-virus": response['data']['attributes']['last_analysis_stats']
                }
            }