from fastapi import FastAPI
import uvicorn
from model import request_body
from service.facade import facade

class Inicar():
    app = FastAPI()
    
    body = request_body

    @app.post('/v1/ip')
    def lambda_handler(ip_address: body.Request):
        facade_service = facade.Facade(ip_address)

        response = facade_service.generate_report()

        return response

    @app.post('/v1/url')
    def lambda_handler(url: body.Request):
        facade_service = facade.Facade(url)

        response = facade_service.generate_report_url()

        return response

    @app.get('/v1/status')
    def status():
        return {"mensagem": "OK"}


    uvicorn.run(app, host='127.0.0.1', port=4443)