import openpyxl
from openpyxl.chart import BarChart,Reference

xlsxfile = openpyxl.Workbook()

data = [
    ('Name', 'Admissions'),
    ('Gone With the Wind', 225.7),
    ('Star Wars', 194.4),
    ('ET: The Extraterrestrial',161.0)
]
sheet = xlsxfile['Sheet']
for row in data:
    sheet.append(row)

chart = BarChart()
chart.title = 'Admissions per movie'
chart.y_axis.title = 'Millions'

data = Reference(sheet,min_row=2,max_row=4,min_col=1,max_col=2)
chart.add_data(data,from_rows=True,titles_from_data=True)

sheet.add_chart(chart,"A6")
xlsxfile.save('movie_chart.xlsx')