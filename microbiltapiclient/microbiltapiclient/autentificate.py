import requests
import json

def autentification(client_id, client_secret, baseURL = 'https://api.microbilt.com'):
    autObj = {'client_id': client_id, 'client_secret': client_secret, 'grant_type': 'client_credentials'}
    with requests.post(baseURL + '/OAuth/GetAccessToken', json = autObj, headers={'Content-Type':'application/json', 'Accept':'application/json'}) as response:
        return json.loads(response.content)['access_token']
