import requests
import json
from utils import credenciais
from utils import urls

class CriminalIP_API:
    def get_report(criminal):
        
        api_url = urls
        api_key = credenciais
        
        URL = api_url.URL.URL_CRIMINAL_IP

        headers = {
            "x-api-key": api_key.Credenciais.API_3
        }

        params = {
            "ip": criminal,
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
        
        api_url = urls
        api_key = credenciais
        
        URL = api_url.URL.URL_CRIMINAL_IP_URL

        headers = {
            "x-api-key": api_key.Credenciais.API_3
        }

        params = {
            "query": criminal,
            "offset": 1
        }

        response = json.loads(requests.get(url=URL, params=params, headers=headers).content)
        print(response)
        return{
            "Criminal IP": {
                "data": response
            }
        }