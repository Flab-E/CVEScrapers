import requests
from lxml import html, etree

base = 'https://support.dlink.com'
url = 'https://support.dlink.com/resource/products/'

res = requests.get(url)
tree = html.fromstring(res.text)

linkList = []
links = [base + _.get('href') for _ in tree.xpath('//a')]
# print(links)

for link in links:
  subRes = requests.get(link)
  subTree = html.fromstring(subRes.text)
  subLinks = [base+_.get('href') for _ in subTree.xpath('//a')]

  for subLink in subLinks:
    if 'notice' in subLink.lower():
      print(subLink)