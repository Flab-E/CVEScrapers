import requests
from bs4 import BeautifulSoup
import time

cveList = [
  "CVE-2021-31802",
  "CVE-2017-6334",
  "CVE-2017-6077",
  "CVE-2017-5521",
  "CVE-2016-1555",
  "CVE-2023-34563",
  "CVE-2016-6277"
]

api = "https://kb.netgear.com/services/apexrest/articlevulnerability?lang=en_US&articlescount=400&articleclassification=Security%20Vulnerability"
headers = {
  "accept":"application/json, text/javascript, */*; q=0.01"
}

response = requests.get(api, headers=headers)

cveURLs = []
for item in response.json():
  cveURLs.append(item['FULLUrl'])

for url in cveURLs:
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  cve = soup.find('div', class_='article-content')

  if url == 'https://kb.netgear.com/000063636/Security-Advisory-for-Authentication-Bypass-on-Multiple-Products-PSV-2021-0084':
    print('FOUND FOUND FOUND')
  
  # for para in cve.find_all('p'):
  #   if 'Associated CVE' in para.text and 'CVE-' in para.text:
  #     cveID = 'CVE-' + para.text.split('CVE-')[-1]
  #     print(f'========= {cveID} =========')
  #     print(url, cveID)

  #     if cveID in cveList:
  #       print('Found:', cveID)
  #     time.sleep(1)
  #     break
  