from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
import argparse

parser = argparse.ArgumentParser(description='Example: Excel.py 19011200020001')
parser.add_argument("-s","--serial",metavar='',help="Serialnumber from Matas.",required=False,default="")
group = parser.add_mutually_exclusive_group()
group.add_argument('-q','--quiet',action='store_true',help='App is quiet')
group.add_argument('-v','--verbose',action='store_true',help='App is quiet')
args = parser.parse_args()

matasqr = 19011200020001

wb = load_workbook(filename = 'Workbook.xlsx')
sheet = wb['Sheet1']

def getdatafromcell():
    for i in range(1,3):
        sheet.cell(row=3,column=2).value = matasqr
        print(sheet.cell(row=3,column=i).value)

if __name__ == "__main__":
    
    if args.quiet:
        sheet.cell(row=3,column=2).value = matasqr
    elif args.verbose:
        print("Sheet names:")
        print(wb.sheetnames)
        print("Get Data from row 1 to 2:")
        getdatafromcell()
    else:
        print("this is else")

    

    #print(sheet_ranges['A1'].value)
    #print(sheet_ranges['B1'].value)

    wb.save('WorkbookPy.xlsx')