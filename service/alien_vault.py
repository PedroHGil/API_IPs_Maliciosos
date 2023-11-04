import requests
import json

def get_alien(request_body):
    
    URL = "https://otx.alienvault.com/api/v1/indicators/submit_url"

    body = {"$schema": "http://json-schema.org/draft-04/schema",
            "additionalParameters": False,
            "required": ["url"],
            "parameters": {
                "url": request_body.ip,
                "tlp": 1
            }
         }

    
    headers = {'X-OTX-API-KEY':'c282ce1a7bc2925e9ac187a28171f3e257cd61304ce54ff20e0684227704a9e7'}
    
    response = requests.get(URL, body=body, headers=headers)
    
    print(response.json())