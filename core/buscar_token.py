import requests
import os

def buscar_token(crt, key, tipo_chamada, client_id=None, secret_key=None, header:list = None, dados: dict = None):    
     
    with open('arquivos/certificado.crt', 'w') as file:
        file.write(crt)
        
            
    with open('arquivos/certificado.key', 'w') as file:
        file.write(key)
        
    try:
        if tipo_chamada == 'Token':

            url = "https://sts.itau.com.br/api/oauth/token"
            payload = f'grant_type=client_credentials&client_id={client_id}&client_secret={secret_key}'
            headers = {
                'x-itau-flowID': "1",
                'x-itau-correlationID': "2",
                'Content-Type': 'application/x-www-form-urlencoded'
            }

            
            response = requests.post(url=url, data=payload, headers=headers, cert=('arquivos/certificado.crt', 'arquivos/certificado.key' ))
                

            if 200 != response.status_code:
                print(response.headers)
            
            return response.json()

        elif tipo_chamada == 'Boleto':
            url = "https://api.itau.com.br/cash_management/v2/boletos"
            payload = dados
            print(header)
            headers = {
                "Authorization":header[0],
                "Content-Type":header[1],
                "x-itau-apikey":header[2], 
                "x-itau-flowID":header[3], 
                "x-itau-correlationID":header[4]}
            
            # Passa os arquivos temporários como cert
            
            response = requests.post(url=url, json=payload, headers=headers, cert=('arquivos/certificado.crt', 'arquivos/certificado.key'))
                
            
            if 200 != response.status_code:
                print(response.headers)
            
            
            return response.json()
    finally:
     
    
        if os.path.exists('arquivos/certificado.crt'):
            os.remove('arquivos/certificado.crt')
        if os.path.exists('arquivos/certificado.key'):
            os.remove('arquivos/certificado.key')