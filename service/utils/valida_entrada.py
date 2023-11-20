import re


class ValidaEntrada():
    
    def __init__(self):
        pass
    
    def validacoes(self, entrada, tipo):
        if tipo == 0:
            if re.search('[a-zA-Z]', entrada):
                raise Exception("IP nao pode conter letras")
        else:
            if 'http://' in entrada or 'https://' in entrada:
                raise Exception("URL nao pode conter HTTPS:// ou HTTP:// use apenas www")
