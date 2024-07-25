import requests
from dotenv import load_dotenv
import os
import time
import json
import pandas as pd

load_dotenv()


def getCVE(cve_id):
  url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
  params = f"?cveId={cve_id}"
  headers = {
    'User-Agent': 'Mozilla/5.0',
    # 'Authorization': "Bearer " + os.getenv("TOKEN"),
    'accept' : '*/*'
  }
  response = requests.request("GET", url + params, headers=headers)
  try:
    return response.json()
  except:
    print(response.text)
    return {'status': 'err'}

def main():
  cveList = [
    "CVE-2019-15060",
    "CVE-2019-17147",
    "CVE-2019-6989",
    "CVE-2020-35576",
    "CVE-2020-8423",
    "CVE-2021-29280",
    "CVE-2021-35003",
    "CVE-2021-41653",
    "CVE-2021-46122",
    "CVE-2022-0650",
    "CVE-2022-24355",
    "CVE-2022-24973",
    "CVE-2022-25062",
    "CVE-2022-25064",
    "CVE-2022-25073",
    "CVE-2022-25074",
    "CVE-2022-26639",
    "CVE-2022-26640",
    "CVE-2022-26641",
    "CVE-2022-26642",
    "CVE-2022-30024",
    "CVE-2022-33087",
    "CVE-2022-4498",
    "CVE-2022-46428",
    "CVE-2022-46430",
    "CVE-2022-46435",
    "CVE-2022-46912",
    "CVE-2022-48194",
    "CVE-2023-30383",
    "CVE-2023-33536",
    "CVE-2023-33537",
    "CVE-2023-36354",
    "CVE-2023-36355",
    "CVE-2023-36358",
    "CVE-2023-36359",
    "CVE-2023-39745",
    "CVE-2023-39747"
  ]

  count = 1
  for cve in cveList:
    if count % 5 == 0:
      print('waiting for 60 seconds...\n')
      time.sleep(60)

    res = getCVE(cve)
    if 'status' in res and res['status'] == 'err':
      return

    des = None
    for desc in res['vulnerabilities'][0]['cve']['descriptions']:
      if desc['lang'] == 'en':
        des = desc['value']
    
    if 'TP-Link' in des:
      des = des.split('TP-Link ')[1].split(' ')[0]
    elif 'TP-LINK' in des:
      des = des.split('TP-LINK ')[1].split(' ')[0]
    print(f"{cve}: {des.split('TP-Link ')[1].split(' ')[0] if 'TP-Link' in des else des}")
    print()

    count += 1

if __name__ == "__main__":
  main()