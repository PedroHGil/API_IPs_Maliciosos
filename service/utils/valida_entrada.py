import re


class ValidaEntrada():
    
    def __init__(self):
        pass
                
    def validacao_url(self, entrada):  
        if entrada is None:
            raise Exception("URL nao pode nula")
        
        if re.search('[0-9][0-9.]*[0-9]', entrada):
            raise Exception("URL nao pode ser um IP")
             
        if 'http://' in entrada or 'https://' in entrada:
            raise Exception("URL nao pode conter HTTPS:// ou HTTP:// use apenas www")

    def validacao_ip(self, entrada):
        if entrada is None:
            raise Exception("IP nao pode nulo")
        
        if re.search('[a-zA-Z]', entrada):
            raise Exception("IP nao pode conter letras")
        
            