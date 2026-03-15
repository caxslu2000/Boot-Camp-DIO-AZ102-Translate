import requests
import os
from docx import Document

subscription_key = ""
endpoint = 'https://api.cognitive.microsofttranslator.com/'
location = "eastus"
language_destination = 'pt-br' 

def translator_text(text, target_language):
    path = '/translate'
    constructed_url = endpoint + path
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(os.urandom(16))
    }
    body = [{
        'text': text
    }]
    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': target_language
    }
    
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    
    # Verificação de erro ---
    # Se a resposta for um dicionário e contiver a palavra 'error', a API barrou a requisição.
    if isinstance(response, dict) and 'error' in response:
        print(f"🚨 A API retornou um erro: {response['error']['message']}")
        return None
        
    # Se não houver erro, retornamos o texto normalmente!
    return response[0]["translations"][0]["text"]

# Testando
resultado = translator_text("I know you're somewhere out there, somewhere far away", language_destination)
if resultado:
    print(f"Tradução: {resultado}")
