import requests
import json

def get_abuse(abuse):   
    url = 'https://api.abuseipdb.com/api/v2/check'
    
    headers = {
         'Accept': 'application/json',
         'Key': '56121366dc68a581f3d33cea839bb12dbf17ab3f9d9a3d931d7e0a5077d8e7b3fe70bf9128113e19'
     }
    querystring = {
     'ipAddress': abuse.ip,
     'maxAgeInDays': '90'
     }
    response = json.loads(requests.get(url=url, headers=headers, params=querystring).text)
    return {"malicioso": response['data']['abuseConfidenceScore'],
            "ip": response['data']['ipAddress'],
            "Dominio": response['data']['domain'],
            "País": response['data']['countryCode'],
            "Tipo": response['data']['usageType']
            }

#response = requests.request(method='GET', url=url, headers=headers, params=querystring)

# Formatted output
#decodedResponse = json.loads(response.text)
#print (json.dumps(decodedResponse, sort_keys=True, indent=4))