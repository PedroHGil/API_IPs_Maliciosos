import requests
import json

#link da documentação da API: https://urlscan.io/docs/api/

def get_urlscan(urlscan):
    headers = {'API-Key':'9c19493a-d762-4b76-9b9f-d54b83d91840',
               'Content-Type':'application/json'
               }

    data = {"url": urlscan.ip, 
            "visibility": "public"
            }

    response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))

    return{
            "useragent": response['options']['useragent'],
            "tags": response['tags']
        }

    #print(response)
    #print(response.json())