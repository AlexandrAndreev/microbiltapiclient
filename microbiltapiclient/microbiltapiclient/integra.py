from .mbrequest import makeget, makepost

class IntegraClient:
    apiName = 'Integra'

    def __init__(self, access_token, baseURL):
        self.access_token = access_token
        self.apiUrl = baseURL
    def quicktrendsreport(self, requestbody):
        return makepost(self.access_token,requestbody,self.apiUrl,self.apiName,'QuickTrendsReport')
    def outlookreport(self, requestbody):
        return makepost(self.access_token,requestbody,self.apiUrl,self.apiName,'OutlookReport')
    def threeyearreport(self, requestbody):
        return makepost(self.access_token,requestbody,self.apiUrl,self.apiName,'ThreeYearReport')
    def fiveyearreport(self, requestbody):
        return makepost(self.access_token,requestbody,self.apiUrl,self.apiName,'FiveYearReport')
    def ocd1report(self, requestbody):
        return makepost(self.access_token,requestbody,self.apiUrl,self.apiName,'Ocd1Report')
    def getdocument(self, fileName):
        return makeget(self.access_token,self.apiUrl,self.apiName,'GetDocument/'+'{' + fileName + '}')