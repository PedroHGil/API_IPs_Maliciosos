import requests
import json

def get_criminal(criminal):
    URL = "https://api.criminalip.io/v1/ip/data"

    headers = {
        "x-api-key": "PoYvjmBaHBNH6Gp7yIhFcpzK65FGdtKS9sbFKxElkshQyMdwWcrlMXeW7iwx"
    }

    params = {
        "ip": criminal.ip,
        "full": False
    }

    response = json.loads(requests.get(url=URL, params=params, headers=headers).content)

    return{
        "WHOIS": response['whois'],
        "VULNERABILITY": response['vulnerability']
    }

    #print(saida)