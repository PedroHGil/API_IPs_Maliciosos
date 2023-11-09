from fastapi import FastAPI
import uvicorn
from service import abuse_ip
from service import virus_total
from model import request_body
from service import url_scan
from service import criminal_ip

app = FastAPI()

@app.post('/v1')
def lambda_handler(ip_adress: request_body.IP):
    response = {"ABuseIP": abuse_ip.get_abuse(ip_adress), 
                "VirusTotal": virus_total.get_virus(ip_adress),
                "CriminalIP": criminal_ip.get_criminal(ip_adress)
               }
    
    return response

@app.post('/v2')
def lambda_handler(ip_adress: request_body.IP):
    response = {"URLScan": url_scan.get_urlscan(ip_adress)
               }
    return response


@app.get('/v1/status')
def status():
    return {"mensagem": "OK"}


uvicorn.run(app, host='127.0.0.1', port=4443)