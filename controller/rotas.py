from fastapi import FastAPI
import uvicorn
from model import request_body
from service.facade import facade

class Inicar():
    
    app = FastAPI()

    @app.post('/v1/ip')
    def rota_ip(ip_address: request_body.Request):
        facade_service = facade.Facade(ip_address)

        response = facade_service.generate_report(tipo=0)

        return response

    @app.post('/v1/url')
    def rota_url(url:  request_body.Request):
        facade_service = facade.Facade(url)

        response = facade_service.generate_report(tipo=1)

        return response

    @app.get('/v1/status')
    def status():
        return {"mensagem": "OK"}


    uvicorn.run(app, host='127.0.0.1', port=4443)