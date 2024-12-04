from .mbrequest import makeget, makepost, makeput

class ComplyTraqClient:
    apiName = 'ComplyTraq'

    def __init__(self, access_token, baseURL):
        self.access_token = access_token
        self.apiUrl = baseURL
    
    def login(self, logininformation):
        self.authentication = makepost(self.access_token,logininformation,self.apiUrl,self.apiName,'auth/login')['token']
    def inspection(self, requestbody):
        return makepost(self.access_token,requestbody,self.apiUrl,self.apiName,'inspection', headerparam={'Authentication':self.authentication})
    def inspectionstatus(self, inspectionId):
        return makeget(self.access_token,self.apiUrl,self.apiName,'inspection/status/'+inspectionId, headerparam={'Authentication':self.authentication})
    def inspectionreport(self, inspectionId):
        return makeget(self.access_token,self.apiUrl,self.apiName,'inspection/report/'+inspectionId, headerparam={'Authentication':self.authentication})
    def attachmentarchive(self, inspectionId):
        return makeget(self.access_token,self.apiUrl,self.apiName,'attachment/archive/'+inspectionId, headerparam={'Authentication':self.authentication})
    def systeminspectionstatuslist(self):
        return makeget(self.access_token,self.apiUrl,self.apiName,'system/inspectionstatus/list', headerparam={'Authentication':self.authentication})
    def customerproductlist(self):
        return makeget(self.access_token,self.apiUrl,self.apiName,'customerproduct/list', headerparam={'Authentication':self.authentication})
    def divisionlist(self):
        return makeget(self.access_token,self.apiUrl,self.apiName,'division/list', headerparam={'Authentication':self.authentication})
    def statelist(self):
        return makeget(self.access_token,self.apiUrl,self.apiName,'state/list', headerparam={'Authentication':self.authentication})