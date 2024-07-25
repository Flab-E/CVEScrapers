import requests
from dotenv import load_dotenv
import os
import time
import json
import pandas as pd

load_dotenv()

# search cve by vendor only: /search?vendorId=834                       Netgear: 834
# search cve by vendor, product and version: /vulnerability/list-by-vpv
# get cve info: /vulnerability/info

vendorMap = {
    "netgear": 834,
    "dlink": 9740,
    "linksys": 833,
    "tplink": 11936,
    "tenda": 13620,
    "asus": 3447
}

def getCVE(cve_id):
    url = "https://www.cvedetails.com/api/v1/vulnerability/info"
    params = f"?cveId={cve_id}"
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Authorization': "Bearer " + os.getenv("TOKEN"),
        'accept' : '*/*'
    }
    response = requests.request("GET", url + params, headers=headers)
    return response.json()

def getCVEsByVendor(vendor):
    global vendorMap
    vendorRes = []

    pageNumber = 1
    resultsPerPage = 50
    while True:
        if pageNumber%5 == 1:
            print('Reached limit. Waiting for a minute')
            time.sleep(61)


        url = "https://www.cvedetails.com/api/v1/vulnerability/search?"
        params = {
            "pageNumber": pageNumber,
            "resultsPerPage": resultsPerPage,
            "isOverflow": 1,
            'isMemoryCorruption': 1,
            'isCodeExecution': 1,
            "vendorId": vendorMap[vendor]
        }
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Authorization': "Bearer " + os.getenv("TOKEN"),
            'accept' : '*/*'
        }
        print(url + '&'.join([f"{_}={params[_]}" for _ in params]))
        response = requests.request("GET", url + '&'.join([f"{_}={params[_]}" for _ in params]), headers=headers)
        try:
            pageRes = response.json()
        except json.decoder.JSONDecodeError:
            print(response.text)
            return -1
        if 'results' in pageRes:
            vendorRes += pageRes['results']
        else:
            print(f'Results json keys: {pageRes.keys()}')

        if 'errors' in pageRes:
            # print(pageNumber)
            print(pageRes['errors'])
            break
        elif 'results' not in pageRes:
            print(f'Results json keys: {pageRes.keys()}')
        elif 'results' in pageRes and len(pageRes['results']) < 50:
            break
        else:
            pageNumber += 1

    print(f'Got {len(vendorRes)} CVEs for {vendor}\n')
    with open(f'{vendor}CVEs.json', 'w') as f:
        json.dump(vendorRes, f, indent=2)

    # in vendorRes keep only vendor, cveId, cveYear, summary, isOverflow, isMemoryCorruption, isCodeExecution
    vendorRes = [{k: _[k] for k in ['vendor', 'cveId', 'cveYear', 'summary', 'isOverflow', 'isMemoryCorruption', 'isCodeExecution']} for _ in vendorRes]
    df = pd.DataFrame(vendorRes)
    df.to_csv(f'{vendor}CVEs.csv', index=False)

    return vendorRes

def getCVEsPost2019(vendor):
    global vendorMap
    vendorRes = []

    pageNumber = 1
    resultsPerPage = 50
    while True:
        if pageNumber%5 == 1:
            print('Reached limit. Waiting for a minute')
            time.sleep(61)


        url = "https://www.cvedetails.com/api/v1/vulnerability/search"
        
        params = {
            "pageNumber": pageNumber,
            "resultsPerPage": resultsPerPage,
            "isOverflow": 1,
            'isMemoryCorruption': 1,
            'isCodeExecution': 1,
            "vendorId": vendorMap[vendor]
        }
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Authorization': "Bearer " + os.getenv("TOKEN"),
            'accept' : '*/*'
        }
        searchURL = url + '?' + '&'.join([f'{_}={params[_]}' for _ in params])
        print(searchURL)
        response = requests.request("GET", searchURL, headers=headers)
        try:
            pageRes = response.json()
        except json.decoder.JSONDecodeError:
            print(response.text)
            return -1
        
        if 'results' in pageRes:
            for res in pageRes['results']:
                if int(res['cveYear']) >= 2019:
                    vendorRes += [res]
                    # print(res)

        if 'errors' in pageRes:
            # print(pageNumber)
            print(pageRes['errors'])
            break
        elif 'results' not in pageRes:
            print(f'Results json keys: {pageRes.keys()}')
        elif 'results' in pageRes and len(pageRes['results']) < 50:
            break
        else:
            pageNumber += 1
    print(f'Got {len(vendorRes)} CVEs for {vendor}\n')
    
    
    with open(f'{vendor}CVEs_after2019.json', 'w') as f:
        json.dump(vendorRes, f, indent=2)

    # in vendorRes keep only vendor, cveId, cveYear, summary, isOverflow, isMemoryCorruption, isCodeExecution
    vendorRes = [{k: _[k] for k in ['vendor', 'cveId', 'cveYear', 'summary', 'isOverflow', 'isMemoryCorruption', 'isCodeExecution']} for _ in vendorRes]
    df = pd.DataFrame(vendorRes)
    df.to_csv(f'{vendor}CVEs_after2019.csv', index=False)
    

    return vendorRes

def allCVES():
    allCVEs = []
    for vendor in ['netgear', 'dlink', 'tenda', 'tplink', 'linksys', 'asus']:
        allCVEs += getCVEsByVendor(vendor)

    df = pd.DataFrame(allCVEs)
    df.to_csv('allCVEs.csv', index=False)
    
print('Using token for ID ', os.getenv('TOKENID'))
# print(getCVEsPost2019("netgear"))
# for vendor in ['netgear', 'dlink', 'tenda', 'tplink', 'linksys', 'asus']:
#     getCVEsPost2019(vendor)
    # getCVEsByVendor(vendor)
# print(get_cve_info("CVE-2024-30572"))

allCVES()