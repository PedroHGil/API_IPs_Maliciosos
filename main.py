from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import AbuseIP
import VirusTotal

app = FastAPI()

class IP (BaseModel):
    ip: str

@app.post('/v1')
def lambda_handler(abuse: IP):
    response = AbuseIP.get_abuse(abuse)
    response2 = VirusTotal.get_virus(abuse)
    response.update(response2)
    return response

@app.get('/v1/status')
def status():
    return {"mensagem": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=4443)