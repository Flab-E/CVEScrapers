import tabula

# read the table from the pdf file
df = tabula.read_pdf("Netgear_EOL.pdf", pages='all')

# print the table
print(df)
