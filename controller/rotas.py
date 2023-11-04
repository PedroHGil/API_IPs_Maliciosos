from fastapi import FastAPI
import uvicorn
from service import abuse_ip
from service import virus_total
from model import request_body
from service import alien_vault

app = FastAPI()

@app.post('/v1')
def lambda_handler(ip_adress: request_body.IP):
    alien_vault.get_alien(ip_adress)
    response = {"ABuseIP": abuse_ip.get_abuse(ip_adress), 
                "VirusTotal": virus_total.get_virus(ip_adress)
               }
    
    return response

@app.get('/v1/status')
def status():
    return {"mensagem": "OK"}


uvicorn.run(app, host='127.0.0.1', port=4443)