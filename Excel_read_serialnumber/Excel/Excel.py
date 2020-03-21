#----Imports----#
from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
import argparse

#----Arg parsing----#
parser = argparse.ArgumentParser(description='Example: Excel.py 19011200020001')
parser.add_argument("-s","--serial",metavar='',help="Serialnumber from Matas.",required=True)
group = parser.add_mutually_exclusive_group()
group.add_argument('-q','--quiet',action='store_true',help='App is quiet')
group.add_argument('-v','--verbose',action='store_true',help='App is quiet')
args = parser.parse_args()

#----Arg mapping----#
matasqr = args.serial

#----Workbook and sheet loading----#
wb = load_workbook(filename = 'Workbook.xlsx')
sheet = wb['Sheet1']
sheet._number_formats = '0.00E+00'
row_count = sheet.max_row
column_count = sheet.max_column

#----Functions----#
def itterate():
    for i in range(1,row_count+1):
        print(sheet.cell(row=i,column=1).value)
    for i in range(1,column_count+1):
        print(sheet.cell(row=1,column=i).value)

def linkserial():
    print("in itterate function")
    print("Using Serial: " + args.serial)
    for i in range(1,row_count):
        sheet.cell(row=i,column=2).value = matasqr
    if sheet.cell is None:
        print("Cell is empty")
    else:
        print("Cell contains data") 

#----Main----#
if __name__ == "__main__":
    
    if args.quiet:
        sheet.cell(row=3,column=2).value = matasqr
    elif args.verbose:
        print("Sheet names:")
        print(wb.sheetnames)
        itterate()
    elif args.serial:
        linkserial()
    else:
        print("this is else")


    #----Save changes to different .xlsx to prevent overriding data----#
    wb.save('WorkbookPy.xlsx')