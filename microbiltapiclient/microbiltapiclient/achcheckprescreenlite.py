from .mbrequest import makeget, makepost

class ACHCheckPrescreenLiteClient:
    apiName = 'ACHCheckPrescreenLite'

    def __init__(self, access_token, baseURL):
        self.access_token = access_token
        self.apiUrl = baseURL
    def getreport(self, requestbody):
        return makepost(self.access_token,requestbody,self.apiUrl,self.apiName,'GetReport')
    def getarchivereport(self, requestbody):
        return makeget(self.access_token,self.apiUrl,self.apiName,'GetArchiveReport')
    def reportperformance(self, requestbody):
        return makepost(self.access_token,requestbody,self.apiUrl,self.apiName,'ReportPerformance')