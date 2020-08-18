import requests
import sys

if len(sys.argv) > 1:
    port = sys.argv[1]
else:
    port = input('Enter port (E.g. 5000):')
    
host = 'http://192.168.1.36' 

AssetCode = None 
#url = '%s:%s/contracts' % (host, port)
# Needs Ubuntu Firewall opened

url = '%s:%s/activateshcapi/covid19greenlight/dlypka/UseExistingWallets' % (host, port)
r = requests.get(url)
print(str(r.status_code))
print('--End of call to activateshcapi()--\n\n')
   
is_createshcsmartcontract_enabled = False
if is_createshcsmartcontract_enabled:
    url = '%s:%s/createshcsmartcontract' % (host, port)
    r = requests.post(url, json={'smartcontract_name': 'covid19greenlight', 'CLIENT_CONTRACT_ADDRESS': '1QAinrbEfjv46jdpwZcqc1nB4tWH9AE8in'})
    print(str(r.status_code))
    print('--End of call to createshcsmartcontract()--\n\n')
    #input('Press any key to Terminate:')
    #exit(0    

is_shareholder_post_enabled = False
if is_shareholder_post_enabled:    
    url = '%s:%s/shareholder' % (host, port)
    r = requests.post(url, json={'smartcontract_name': 'covid19greenlight', 'CLIENT_CONTRACT_ADDRESS': '1QAinrbEfjv46jdpwZcqc1nB4tWH9AE8in', 'shareholder_name': 'Warren Buffet', 'shareholder_shortname': 'wbuffet'})
    print(str(r.status_code))
    print('--End of call to shareholder()--\n\n')
    #input('Press any key to Terminate:')
    #exit(0)
    
   
is_asset_post_enabled = True
if is_asset_post_enabled:    
    url = '%s:%s/asset' % (host, port)
    # have to include the contents of
    #  asset_payload_filepath = base_contract_json_path + '/covid19greenlight_asset_payload_SHC.json'
    """
    {"Ticker": "GRNLT", "Description": "COVID19Greenlight.org"}
    """  
    #  covid19greenlight_asset_definition_SHC.json
    """
    {"TransfersPermitted": true, "EnforcementOrdersPermitted": true, "TradeRestrictions": ["AUS"], "VotingRights": true, "VoteMultiplier": 1, "AdministrationProposal": true, "HolderProposal": true, "AssetModificationGovernance": 1, "TokenQty": 256000, "AssetType": "SHC", "AssetPayload": "0a0547524e4c541a15434f5649443139477265656e6c696768742e6f7267"}
    """
    r = requests.post(url, json={'smartcontract_name': 'covid19greenlight', 
                                 'CLIENT_CONTRACT_ADDRESS': '1QAinrbEfjv46jdpwZcqc1nB4tWH9AE8in', 
                                 'shareholder_name': 'Warren Buffet', 
                                 'shareholder_shortname': 'wbuffet', 
                                 'asset_payload': {"Ticker": "GRNLT", "Description": "COVID19Greenlight.org"},
                                 'asset_definition': {"TransfersPermitted": True, "EnforcementOrdersPermitted": True, "TradeRestrictions": ["AUS"], "VotingRights": True, "VoteMultiplier": 1, "AdministrationProposal": True, "HolderProposal": True, "AssetModificationGovernance": 1, "TokenQty": 256000, "AssetType": "SHC"}},
                   )
    # See response properties of r in https://www.w3schools.com/python/ref_requests_response.asp
    print(str(r.status_code))
    responsejson = r.json()
    AssetCode = responsejson['AssetCode']
    print('AssetCode=%s' % AssetCode)
    print('--End of call to asset()--\n\n')
    input('Press any key to Terminate:')
    exit(0)    

is_airdrop_enabled = False
if is_airdrop_enabled:
    if not AssetCode:
        print('Missing AssetCode value.  Please request /asset first.')
        input('Press any key to Terminate:')
        exit(1)
    url = '%s:%s/airdrop' % (host, port)
    r = requests.post(url, json={'smartcontract_name': 'covid19greenlight', 'CLIENT_CONTRACT_ADDRESS': '1QAinrbEfjv46jdpwZcqc1nB4tWH9AE8in', 'AssetCode': AssetCode, 'shareholder_name': 'Warren Buffet', 'shareholder_shortname': 'wbuffet', 'shareholder_moniker': 'wbuffet_13f4SpiGcvPa2ko6noeTj8fFKTJ8M2So6f'})
    print(str(r.status_code))
    print('--End of call to shareholder()--\n\n')
    input('Press any key to Terminate:')
    exit(0)



