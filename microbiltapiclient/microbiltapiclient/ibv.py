from .mbrequest import makeget, makepost

class IBVClient:
    apiName = 'IBV'

    def __init__(self, access_token, baseURL):
        self.access_token = access_token
        self.apiUrl = baseURL
    def createform(self, requestbody):
        return makepost(self.access_token,requestbody,self.apiUrl,self.apiName,'CreateForm')
    def getreport(self, params):
        return makeget(self.access_token,self.apiUrl,self.apiName,'GetReport', params)