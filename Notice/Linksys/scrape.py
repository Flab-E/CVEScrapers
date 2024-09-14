import requests
import lxml.html as lh

dirtyList = """WAG320N
XAC1900
RE2000v2.0
EA9200v1.0
MR9600v1.0
E900
E2000v1.0
E1000v2.1
E2500
EA7430
WRT54GLETSI
EA6350v2.0
EA8300v1.0_v1.1
EA9300v1.0
E1550v1.0
EA6200v1.0
WRT54G
WHW03v2.0
E4200v1.0
X2000v2.0
E1500
EA9500
E800v1.0
E1700
E1500v1.0
RE2000v1.0
EA7450
E8450v1.0
WRT54GLUS
MR9600v2.0
M10
WRT54GL
EA6300v1.0_US
EA7200
LAPAC1200_LAPAC1750v1.0
MR9600
EA7300
E900v1.0
EA2750
WRT32X
E8450
MX8500v1.0
E7350
EA6900
EA6900v1.1
E5600v1.0
LRT214
EA6350v1.0
EA7500v3.0
WES610N
RE4000Wv1.0
E5400
RE1000v1.0_v1.5
WRT160NV2
E9450
WHW03v1.0
WRT160NL
E2500v4.0
EA9400
E1200
EA6700
WAP610N
WRT3200ACM
MR6350
E3200v1.0
EA4500v3.0
EA7430v1.0
E7350v1.0
LRT224
EA6700v1.0
RE3000v1.0
EA3500
MR7350
EA6500v2.0
X6200
E2100Lv1.0
EA7250v1.0
WUMC710v1.0
EA6900v2.0
MX5300v1.0
EA8100
M20
MR8300v1.0_v1.1
MR7320
EA6350v4.0
RE4100Wv1.0
E1200v1.0
EA9500v2.0
X1000
LAPN300_LAPN600v1.0
WRT320N
MR8300
E2500v3.0
MR7340
EA6400
EA9300
EA4500
EA9500S
E3000v1.0
RE3000v2.0
EA6500v1.0
E8350
MR9000v1.0
EA9400v1.0
EA7400
EA2700v1.0
MR9000
EA7500
PLW400v1
EA6350
E1200v2.0
E8400
RE1000v2.0
WRT32Xv1.0
EA6400v1.0
EA2700
EA9200
EA6500
E2500v2.0"""

url = "https://store.linksys.com/hk/Linksys-products-end-of-life.html"
page = requests.get(url)
doc = lh.fromstring(page.content)

# use etree to get the last table in the doc
table = doc.xpath('//table')[-1]
# get the rows from the table
tr_elements = table.xpath('.//tr')
dateMap = {
  "Jan": "1",
  "Feb": "2",
  "Mar": "3",
  "Apr": "4",
  "May": "5",
  "Jun": "6",
  "Jul": "7",
  "Aug": "8",
  "Sep": "9",
  "Oct": "10",
  "Nov": "11",
  "Dec": "12"
}

dirtyList = dirtyList.split("\n")
for router in dirtyList:
  original = router
  router = router.split('.')[0][:-2]

  found = 0
  for tr in tr_elements:
    cells = tr.xpath('.//td')
    if len(cells)>0 and router == cells[0].text_content():
      rawDate = cells[-1].text_content()
      day = rawDate.split("-")[0]
      month = dateMap[rawDate.split("-")[1]]
      year = rawDate.split("-")[2]
      print(f"{day},{month},{year},", router)
      found = 1

  if not found:
    print("-,-,-,", original)
  