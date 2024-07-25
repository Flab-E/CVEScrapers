from lxml import etree

# read eolraw.html file and parse it to lxml etree using html parser
# extract the table and write it to a csv file
raw = open('eolraw.html').read()
raw = raw.split('\n')[2165]

html = etree.HTML(raw, parser=etree.HTMLParser())\

# table with id myTable
table = html.xpath('//table[@id="myTable"]')[0]
rows = table.xpath('.//tbody/tr')

dat = 'sku, description, model, sku region, lifecycle phase, eolDate, eosDate\n'


for row in rows:
  cols = row.xpath('.//td')
  sku = cols[0].text.replace('\n', '\t').replace(',', '.')
  desc = cols[1].text.replace('\n', '\t').replace(',', '.')
  model = cols[2].text.replace('\n', '\t').replace(',', '.')
  region = cols[3].text.replace('\n', '\t').replace(',', '.')
  phase = cols[4].text.replace('\n', '\t').replace(',', '.')
  eolDate = cols[5].text.replace('\n', '\t').replace(',', '.')

  if len(cols) > 6:
    eosDate = cols[6].text
  else:
    eosDate = '-'
    
  dat += f'{sku}, {desc}, {model}, {region}, {phase}, {eolDate}, {eosDate}\n'

with open('eol.csv', 'w') as f:
  f.write(dat)