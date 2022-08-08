import argparse
import os
import fileinput
import linecache
import json


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


def get_test_result_data() -> str:
    with fileinput.input([args.file]) as logfile:                  
        for text in logfile:
            if '- SN: ' in text:
                text.strip()
                text = text.replace("- SN: ", "")
                SN_DUT = text[0:text.find(" - Location")]#read till Location
                LOCATION_DUT = text[text.find("Location"):text.find("- PN")]
                RESULT_DUT = text[text.find("Result"):len(text)]
                # print(f"{SN_DUT}\n{LOCATION_DUT}\n{RESULT_DUT}")
                serialized_data = {
                        'SN' : [SN_DUT],
                        'LOCATION':[LOCATION_DUT],
                        'RESULT_DUT':[RESULT_DUT]                   
                }
                print(serialized_data)
                
            elif 'TEST FAILURE Failure reason' in text:
                text.strip()
                GET_LOCATION = text[text.find("L"):text.find("S")].strip()
                GET_CURRENT_LINE_NUMBER = logfile.filelineno()
                SET_LINE_NUMBER = linecache.getline(args.file, (GET_CURRENT_LINE_NUMBER+1)).strip()
                REF_DES_ONLY = SET_LINE_NUMBER[SET_LINE_NUMBER.find("Ref"):len(SET_LINE_NUMBER)].strip()
                
                serialized_data = {
                    'LOCATION' : [GET_LOCATION],
                    'REF_DES':[REF_DES_ONLY],              
                }
                serialized_data_json = json.dumps(serialized_data)
                print(serialized_data_json)
get_test_result_data()