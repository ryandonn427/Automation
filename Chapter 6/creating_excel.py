import openpyxl
xlsxfile = openpyxl.Workbook()
print(xlsxfile.sheetnames)

sheet = xlsxfile['Sheet']

data = [
    (225.7,'Gone With the Wind', 'Victor Fleming'),
    (194.4,'Star Wars', 'George Lucas'),
    (161.0,'ET: The Extraterestrial', 'Steven Spielberg')
]

for row,(admissions,name,director) in enumerate(data,2):
    sheet['A{}'.format(row)].value = director
    sheet['B{}'.format(row)].value = name
    
xlsxfile.save('movie_sheets.xlsx')
