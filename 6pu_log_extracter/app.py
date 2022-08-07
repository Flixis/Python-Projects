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

def get_shannon_memtest_fail(set_of_data:int) -> tuple:
    
    shannon_memtest_refdes_array = []
    for lines in logfile:
        if 'Shannon memtest failed' in lines:
            shannon_memtest_refdes_array = lines
            #print(f"found keyword:{shannon_memtest_refdes_array.strip()}") #strip \n
            count = 1
            while count <= set_of_data:
                print(shannon_memtest_refdes_array) 
                count += 1  # This is the same as count = count + 1
                if count >= set_of_data:
                    return True
                
def get_test_result_data() -> str:
    for lines in logfile:
        if '- SN: ' in lines:
            print(f"found keyword: {lines.strip()}")
            
            
def generate_data_struct(shannonmemtest_fail:str , testresults:str) -> str:
    
    
    pass

print(get_shannon_memtest_fail(3))