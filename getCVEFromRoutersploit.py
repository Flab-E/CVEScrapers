import os
import requests

CVEdir = '/home/salty/flabby/sefcom/routersploit_ghpatched/routersploit_ghpatched/routersploit/modules/exploits/routers/'

# get all python files from sub directories
def getFiles():
  files = []
  for root, dirs, file in os.walk(CVEdir):
    # print(root, dirs, file)
    for f in file:
      # print(f)
      if f.endswith('.py'):
        files.append(os.path.join(root, f))
  return files

cveFiles = getFiles()
print('done')

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

cveIdList = []
for f in cveFiles:
  with open(f, 'r') as fi:
    for line in fi:
      if 'references' in line:
        curr = next(fi)
        while ')' not in curr and ']' not in curr:
          if 'CVE' in curr:
            cveId = 'CVE-'+curr.split('CVE-')[1].split(' ')[0][:10]
            if cveId[-1] == '-' or cveId[-1] == '"':
              cveId = cveId[:-1]
            cveIdList += [cveId]
          curr = next(fi)
    fi.close()

for cveId in cveIdList:
  # print(getCVE(cveId))
  # print('done')
  print(cveId)