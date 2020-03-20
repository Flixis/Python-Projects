from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

wb = load_workbook(filename = 'Workbook.xlsx')
print("Sheet names:")
print(wb.sheetnames)
sheet_ranges = wb['Sheet1']

print("Get Data from row 1 to 2:")
for i in range(1,3):
    print(sheet_ranges.cell(row=2,column=i).value)


print(sheet_ranges['A1'].value)
print(sheet_ranges['B1'].value)

wb.save('WorkbookPy.xlsx')