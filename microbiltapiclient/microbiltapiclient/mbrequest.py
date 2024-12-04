from urllib.parse import urlparse, urlencode
import requests
import json

def makeurl(baseurl, apiname, methodname, params = {}):
    urlp = urlparse(baseurl)._replace(path=apiname + '/' + methodname)._replace(query=urlencode(params))    
    return urlp.geturl()

def makeget(access_token, baseurl, apiname, methodname, params = {}, headerparam = {}):
    requesturl = makeurl(baseurl, apiname, methodname, params)
    headers = {'Authorization':'Bearer ' + access_token, 'Content-Type':'application/json', 'Accept':'application/json'}
    headers.update(headerparam)
    with requests.get(requesturl, headers = headers) as response:
        return json.loads(response.content)

def makepost(access_token, requestContent, baseurl, apiname, methodname, params = {}, headerparam = {}):
    requesturl = makeurl(baseurl, apiname, methodname, params)
    headers = {'Authorization':'Bearer ' + access_token, 'Content-Type':'application/json', 'Accept':'application/json'}
    headers.update(headerparam)
    with requests.post(requesturl, json = requestContent, headers = headers) as response:
        return json.loads(response.content)
def makeput(requestContent, baseurl, apiname, methodname, params = {}, headerparam = {}):
    requesturl = makeurl(baseurl, apiname, methodname, params)
    headers = {'Content-Type':'application/json', 'Accept':'application/json'}
    headers.update(headerparam)
    with requests.put(requesturl, json = requestContent, headers = headers) as response:
        return json.loads(response.content)

