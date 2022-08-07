import argparse
import enum
import os
import fileinput


def dir_path(string):
    """
    Checks if the passed string is a dir.
    """
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

parser = argparse.ArgumentParser(description='Example: app.py -f <log_to_scan>')
parser.add_argument("-f","--file",metavar='',help="Log file to scan.",required=True, default=os.getcwd())
args = parser.parse_args()

logfile = fileinput.input([args.file])

def get_shannon_memtest_fail() -> str:
    for lines in logfile:
        if 'Shannon memtest failed' in lines:
            shannon_memtest_refdes_array = lines
                    
            return print(f"found keyword:{shannon_memtest_refdes_array.strip()}") #strip \n
            
            if 'RefDes: ' in lines:
                #renaming lines to shannon_memtest_refdes_array for later use in code.
                shannon_memtest_refdes_array = lines
                #print(f"Keyword: {shannon_memtest_refdes_array}")
                
                
def get_test_result_data() -> str:
    for lines in logfile:
        if '- SN: ' in lines:
            print(f"found keyword: {lines.strip()}")
            

get_test_result_data()