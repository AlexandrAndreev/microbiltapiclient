import microbiltapiclient

mbtst = microbiltapiclient.MicrobiltAPIClient('client_id', 'client_secret')
client = mbtst.abaacctverification()
reportbody = {
  "BankRoutingNumber": "011103093",
  "BankAccountNumber": "9942192099"
}
report = client.getreport(reportbody)
print(report)
