from .mbrequest import makeget, makepost

class NadaVehiclePricingClient:
    apiName = 'NadaVehiclePricing'

    def __init__(self, access_token, baseURL):
        self.access_token = access_token
        self.apiUrl = baseURL
    def getreport(self, requestbody):
        return makepost(self.access_token,requestbody,self.apiUrl,self.apiName,'GetReport')
    def getstates(self):
        return makeget(self.access_token,self.apiUrl,self.apiName,'GetStates')
    def getyears(self):
        return makeget(self.access_token,self.apiUrl,self.apiName,'GetYears')
    def getmake(self, params):
        return makeget(self.access_token,self.apiUrl,self.apiName,'GetMake', params)
    def getseries(self, params):
        return makeget(self.access_token,self.apiUrl,self.apiName,'GetSeries', params)
    def getbody(self, params):
        return makeget(self.access_token,self.apiUrl,self.apiName,'GetBody', params)