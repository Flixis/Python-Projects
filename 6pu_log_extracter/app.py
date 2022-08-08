import argparse
import os
import fileinput
import linecache


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
            text.strip()
            text = text.replace("- ", "")
            SN_DUT = text[0:text.find("Location")]#read till Location
            LOCATION_DUT = text[text.find("Location"):text.find("PN")]
            RESULT_DUT = text[text.find("Result"):len(text)]
            #print(f"{SN_DUT}\n{LOCATION_DUT}\n{RESULT_DUT}")
        if 'TEST FAILURE Failure reason' in text:
            text.strip()
            GET_LOCATION = text[text.find("L"):text.find("S")]
            GET_LINE_NUMBER = logfile.filelineno()
            SET_LINE_NUMBER = linecache.getline(args.file, (GET_LINE_NUMBER+1))
            print(f"{GET_LOCATION}{GET_LINE_NUMBER}{SET_LINE_NUMBER}")
            # logfile.readline(GET_LINE_NUMBER)
            
            

get_test_result_data()
fileinput.close()