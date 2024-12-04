from .autentificate import autentification
from .abaacctverification import ABAAcctVerificationClient
from .achcheckprescreenlite import ACHCheckPrescreenLiteClient
from .addressstandardization import AddressStandardizationClient
from .addressnameverification import AddressNameVerificationClient
from .deathmasterfilevalidation import DeathMasterFileValidationClient
from .dlverify import DLVerifyClient
from .emailsearch import EmailSearchClient
from .emailvalidation import EmailValidationClient
from .integra import IntegraClient
from .ipaddressinfo import IPAddressInfoClient
from .nadavehiclepricing import NadaVehiclePricingClient
from .phonesearch import PhoneSearchClient
from .phoneaddressverification import PhoneAddressVerificationClient
from .phonenameverification import PhoneNameVerificationClient
from .professionallicensesearch import ProfessionalLicenseSearchClient
from .propertysearch import PropertySearchClient
from .reversephonesearch import ReversePhoneSearchClient
from .ssnvalidation import SSNValidationClient
from .ssnaddressverification import SSNAddressVerificationClient
from .ssnnameverification import SSNNameVerificationClient
from .ssnphoneverification import SSNPhoneVerificationClient
from .uccsearchreport import UCCSearchReportClient
from .ofacwatchlistsearch import OFACWatchlistSearchClient
from .achcheckprescreen import ACHCheckPrescreenClient
from .bav import BAVClient
from .bankruptcysearch import BankruptcySearchClient
from .complytraq import ComplyTraqClient
from .dlsearch import DLSearchClient
from .employmentsearch import EmploymentSearchClient
from .enhancedpeoplesearch import EnhancedPeopleSearchClient
from .equifaxca import EquifaxCAClient
from .equifax import EquifaxClient
from .evictionssearch import EvictionsSearchClient
from .experian import ExperianClient
from .achcheckprescreenextended import ACHCheckPrescreenExtendedClient
from .idverify import IDVerifyClient
from .ibv import IBVClient
from .ipredict import iPredictClient
from .mbcr import MBCRClient
from .mbclr import MBCLRClient
from .mlaverify import MLAVerifyClient
from .payrollverification import PayrollVerificationClient
from .bankaccountsearchv2 import BankAccountSearchV2Client
from .tracedetail import TraceDetailClient
from .transunion import TransUnionClient
from .criminalsearchv2 import CriminalSearchV2Client
from .vehiclesearch import VehicleSearchClient

class MicrobiltAPIClient:
    def __init__(self,client_id, client_secret, baseURL = 'https://api.microbilt.com'):
        self.access_token = autentification(client_id, client_secret, baseURL)
        self.baseurl = baseURL
    def abaacctverification(self):
        return ABAAcctVerificationClient(self.access_token, self.baseurl)
    def achcheckprescreenlite(self):
        return ACHCheckPrescreenLiteClient(self.access_token, self.baseurl)
    def addressstandardization(self):
        return AddressStandardizationClient(self.access_token, self.baseurl)
    def addressnameverification(self):
        return AddressNameVerificationClient(self.access_token, self.baseurl)
    def deathmasterfilevalidation(self):
        return DeathMasterFileValidationClient(self.access_token, self.baseurl)
    def dlverify(self):
        return DLVerifyClient(self.access_token, self.baseurl)
    def emailsearch(self):
        return EmailSearchClient(self.access_token, self.baseurl)
    def emailvalidation(self):
        return EmailValidationClient(self.access_token, self.baseurl)
    def integra(self):
        return IntegraClient(self.access_token, self.baseurl)
    def ipaddressinfo(self):
        return IPAddressInfoClient(self.access_token, self.baseurl)
    def nadavehiclepricing(self):
        return NadaVehiclePricingClient(self.access_token, self.baseurl)
    def phonesearch(self):
        return PhoneSearchClient(self.access_token, self.baseurl)
    def phoneaddressverification(self):
        return PhoneAddressVerificationClient(self.access_token, self.baseurl)
    def phonenameverification(self):
        return PhoneNameVerificationClient(self.access_token, self.baseurl)
    def professionallicensesearch(self):
        return ProfessionalLicenseSearchClient(self.access_token, self.baseurl)
    def propertysearch(self):
        return PropertySearchClient(self.access_token, self.baseurl)
    def reversephonesearch(self):
        return ReversePhoneSearchClient(self.access_token, self.baseurl)
    def ssnvalidation(self):
        return SSNValidationClient(self.access_token, self.baseurl)
    def ssnaddressverification(self):
        return SSNAddressVerificationClient(self.access_token, self.baseurl)
    def ssnnameverification(self):
        return SSNNameVerificationClient(self.access_token, self.baseurl)
    def ssnphoneverification(self):
        return SSNPhoneVerificationClient(self.access_token, self.baseurl)
    def uccsearchreport(self):
        return UCCSearchReportClient(self.access_token, self.baseurl)
    def ofacwatchlistsearch(self):
        return OFACWatchlistSearchClient(self.access_token, self.baseurl)
    def achcheckprescreen(self):
        return ACHCheckPrescreenClient(self.access_token, self.baseurl)
    def bav(self):
        return BAVClient(self.access_token, self.baseurl)
    def bankruptcysearch(self):
        return BankruptcySearchClient(self.access_token, self.baseurl)
    def complytraq(self):
        return ComplyTraqClient(self.access_token, self.baseurl)
    def dlsearch(self):
        return DLSearchClient(self.access_token, self.baseurl)
    def employmentsearch(self):
        return EmploymentSearchClient(self.access_token, self.baseurl)
    def enhancedpeoplesearch(self):
        return EnhancedPeopleSearchClient(self.access_token, self.baseurl)
    def equifaxca(self):
        return EquifaxCAClient(self.access_token, self.baseurl)
    def equifax(self):
        return EquifaxClient(self.access_token, self.baseurl)
    def evictionssearch(self):
        return EvictionsSearchClient(self.access_token, self.baseurl)
    def experian(self):
        return ExperianClient(self.access_token, self.baseurl)
    def achcheckprescreenextended(self):
        return ACHCheckPrescreenExtendedClient(self.access_token, self.baseurl)
    def idverify(self):
        return IDVerifyClient(self.access_token, self.baseurl)
    def ibv(self):
        return IBVClient(self.access_token, self.baseurl)
    def ipredict(self):
        return iPredictClient(self.access_token, self.baseurl)
    def mbcr(self):
        return MBCRClient(self.access_token, self.baseurl)
    def mbclr(self):
        return MBCLRClient(self.access_token, self.baseurl)
    def mlaverify(self):
        return MLAVerifyClient(self.access_token, self.baseurl)
    def payrollverification(self):
        return PayrollVerificationClient(self.access_token, self.baseurl)
    def bankaccountsearchv2(self):
        return BankAccountSearchV2Client(self.access_token, self.baseurl)
    def tracedetail(self):
        return TraceDetailClient(self.access_token, self.baseurl)
    def transunion(self):
        return TransUnionClient(self.access_token, self.baseurl)
    def criminalsearchv2(self):
        return CriminalSearchV2Client(self.access_token, self.baseurl)
    def vehiclesearch(self):
        return VehicleSearchClient(self.access_token, self.baseurl)