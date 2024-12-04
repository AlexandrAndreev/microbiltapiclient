from .mbrequest import makeget, makepost

class MLAVerifyClient:
    apiName = 'MLAVerify'

    def __init__(self, access_token, baseURL):
        self.access_token = access_token
        self.apiUrl = baseURL
    def getreport(self, requestbody):
        return makepost(self.access_token,requestbody,self.apiUrl,self.apiName,'GetReport')
    def getarchivereport(self, params):
        return makeget(self.access_token,self.apiUrl,self.apiName,'GetArchiveReport', params)