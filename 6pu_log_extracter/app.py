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

def get_shannon_memtest_fail() -> tuple:
    
    shannon_memtest_refdes_array = []
    for text in logfile:
        if 'Shannon memtest failed' in text:
            shannon_memtest_refdes_array = text
            print(f"{shannon_memtest_refdes_array.strip()}") #strip \n
                
def get_test_result_data() -> str:
    for text in logfile:
        if '- SN: ' in text:
            text = text.replace("- ", "")
            SN_DUT = text[0:text.find("Location")]#read till Location
            LOCATION_DUT = text[text.find("Location"):text.find("PN")]
            RESULT_DUT = text[text.find("Result"):len(text)]
            print(f"{SN_DUT}\n{LOCATION_DUT}\n{RESULT_DUT}")
            
            
def generate_data_struct(shannonmemtest_fail:str , testresults:str) -> str:
    
    
    pass

get_test_result_data()