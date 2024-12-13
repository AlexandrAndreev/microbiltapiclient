# Microbilt APIs Client

A python client for consuming the Microbilt APIs.

For more about APIs You can see on [Microbilt Developer Portal](https://developer.microbilt.com/)

## Implemented APIs in this client:

[ABAAcctVerification](https://developer.microbilt.com/api/ABAAcctVerification)

[ACHCheckPrescreenLite](https://developer.microbilt.com/api/ACHCheckPrescreenLite)

[AddressStandardization](https://developer.microbilt.com/api/AddressStandardization)

[AddressNameVerification](https://developer.microbilt.com/api/AddressNameVerification)

[DeathMasterFileValidation](https://developer.microbilt.com/api/DeathMasterFileValidation)

[DLVerify](https://developer.microbilt.com/api/DLVerify)

[EmailSearch](https://developer.microbilt.com/api/EmailSearch)

[EmailValidation](https://developer.microbilt.com/api/EmailValidation)

[Integra](https://developer.microbilt.com/api/Integra)

[IPAddressInfo](https://developer.microbilt.com/api/IPAddressInfo)

[NadaVehiclePricing](https://developer.microbilt.com/api/NadaVehiclePricing)

[PhoneSearch](https://developer.microbilt.com/api/PhoneSearch)

[PhoneAddressVerification](https://developer.microbilt.com/api/PhoneAddressVerification)

[PhoneNameVerification](https://developer.microbilt.com/api/PhoneNameVerification)

[ProfessionalLicenseSearch](https://developer.microbilt.com/api/ProfessionalLicenseSearch)

[PropertySearch](https://developer.microbilt.com/api/PropertySearch)

[ReversePhoneSearch](https://developer.microbilt.com/api/ReversePhoneSearch)

[SSNValidation](https://developer.microbilt.com/api/SSNValidation)

[SSNAddressVerification](https://developer.microbilt.com/api/SSNAddressVerification)

[SSNNameVerification](https://developer.microbilt.com/api/SSNNameVerification)

[SSNPhoneVerification](https://developer.microbilt.com/api/SSNPhoneVerification)

[UCCSearchReport](https://developer.microbilt.com/api/UCCSearchReport)

[OFACWatchlistSearch](https://developer.microbilt.com/api/OFACWatchlistSearch)

[ACHCheckPrescreen](https://developer.microbilt.com/api/ACHCheckPrescreen)

[BAV](https://developer.microbilt.com/api/BAV)

[BankruptcySearch](https://developer.microbilt.com/api/BankruptcySearch)

[ComplyTraq](https://developer.microbilt.com/api/ComplyTraq)

[DLSearch](https://developer.microbilt.com/api/DLSearch)

[EmploymentSearch](https://developer.microbilt.com/api/EmploymentSearch)

[EnhancedPeopleSearch](https://developer.microbilt.com/api/EnhancedPeopleSearch)

[EquifaxCA](https://developer.microbilt.com/api/EquifaxCA)

[Equifax](https://developer.microbilt.com/api/Equifax)

[EvictionsSearch](https://developer.microbilt.com/api/EvictionsSearch)

[Experian](https://developer.microbilt.com/api/Experian)

[ACHCheckPrescreenExtended](https://developer.microbilt.com/api/ACHCheckPrescreenExtended)

[IDVerify](https://developer.microbilt.com/api/IDVerify)

[IBV](https://developer.microbilt.com/api/IBV)

[iPredict](https://developer.microbilt.com/api/iPredict)

[MBCR](https://developer.microbilt.com/api/MBCR)

[MBCLR](https://developer.microbilt.com/api/MBCLR)

[MLAVerify](https://developer.microbilt.com/api/MLAVerify)

[PayrollVerification](https://developer.microbilt.com/api/PayrollVerification)

[BankAccountSearchV2](https://developer.microbilt.com/api/BankAccountSearchV2)

[TraceDetail](https://developer.microbilt.com/api/TraceDetail)

[TransUnion](https://developer.microbilt.com/api/TransUnion)

[CriminalSearchV2](https://developer.microbilt.com/api/CriminalSearchV2)

[VehicleSearch](https://developer.microbilt.com/api/VehicleSearch)

# You can use this client for all Microbilt APIs plans

## App Verification Package:

[AddressNameVerification](https://developer.microbilt.com/api/AddressNameVerification)

[DeathMasterFileValidation](https://developer.microbilt.com/api/DeathMasterFileValidation)

[DLVerify](https://developer.microbilt.com/api/DLVerify)

[EmailValidation](https://developer.microbilt.com/api/EmailValidation)

[IPAddressInfo](https://developer.microbilt.com/api/IPAddressInfo)

[OFACWatchlistSearch](https://developer.microbilt.com/api/OFACWatchlistSearch)

[PhoneAddressVerification](https://developer.microbilt.com/api/PhoneAddressVerification)

[PhoneNameVerification](https://developer.microbilt.com/api/PhoneNameVerification)

[SSNAddressVerification](https://developer.microbilt.com/api/SSNAddressVerification)

[SSNNameVerification](https://developer.microbilt.com/api/SSNNameVerification)

[SSNPhoneVerification](https://developer.microbilt.com/api/SSNPhoneVerification)

[SSNValidation](https://developer.microbilt.com/api/SSNValidation)

## Bank Account Validation Plan:

[ABAAcctVerification](https://developer.microbilt.com/api/ABAAcctVerification)

## Bank Account Validation 2_Final Plan:

[ACHCheckPrescreenLite](https://developer.microbilt.com/api/ACHCheckPrescreenLite)

## Locate People Package:

[EmailSearch](https://developer.microbilt.com/api/EmailSearch)

[PhoneSearch](https://developer.microbilt.com/api/PhoneSearch)

[ReversePhoneSearch](https://developer.microbilt.com/api/ReversePhoneSearch)

## Locate Assets Package Plan:

[PropertySearch](https://developer.microbilt.com/api/PropertySearch)

## NADA Vehicle Pricing Plan:

[NadaVehiclePricing](https://developer.microbilt.com/api/NadaVehiclePricing)

## Business Credentialing Package Plan:

[ProfessionalLicenseSearch](https://developer.microbilt.com/api/ProfessionalLicenseSearch)

[UCCSearchReport](https://developer.microbilt.com/api/UCCSearchReport)

# Quick Start

```
import microbiltapiclient

mbclient = microbiltapiclient.MicrobiltAPIClient('client_id', 'client_secret')
```
# Configuration

`client_id` required

`client_secret` required

`baseURL` optional (defaults to [Production](https://api.microbilt.com)). Other option is Sandbox microbilt APSs link [https://apitest.microbilt.com](https://apitest.microbilt.com) 

# Usage

For usage you need create plan client with you credentials ```microbiltapiclient.MicrobiltAPIClient('client_id', 'client_secret')```

All APIs implemented like method in ```MicrobiltAPIClient``` class, after call return client for work with API ```abaacctverificationclient = mbclient.abaacctverification()```

## More usage with test call APIs from plan:
```
import microbiltapiclient

mbclient = microbiltapiclient.MicrobiltAPIClient('client_id', 'client_secret')
abaacctverificationclient = mbclient.abaacctverification()

examplereportbody = {
  "BankRoutingNumber": "011103093",
  "BankAccountNumber": "9942192099"
}

report = abaacctverificationclient.getreport(examplereportbody)
```
