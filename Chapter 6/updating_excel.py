import openpyxl
from openpyxl.comments import Comment

xlsxfile = openpyxl.load_workbook('movies.xlsx')
sheet = xlsxfile['Sheet1']

print(sheet['D4'].value)
sheet['D4'].value = 'Spielberg'

sheet['D4'].comment = Comment('Changed text automatically', 'User')
sheet['B12'] = '=SUM(B2:B11)'
xlsxfile.save('movies_comment.xlsx')