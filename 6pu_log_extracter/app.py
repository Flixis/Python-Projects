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
parser.add_argument("-f","--file",metavar='',help="Log file to scan.",required=False, default=os.getcwd())
args = parser.parse_args()





REF_DES_ONLY , RESULT_DUT , GET_LOCATION , LOCATION_DUT , SN_DUT = "","","","",""
with fileinput.input([args.file]) as logfile:
    for text in logfile:
        text.strip()
        if 'TEST FAILURE Failure reason' in text:
            GET_LOCATION = text[text.find("L"):text.find("S")].strip()
            GET_CURRENT_LINE_NUMBER = logfile.filelineno()
            SET_LINE_NUMBER = linecache.getline(args.file, (GET_CURRENT_LINE_NUMBER+1)).strip()
            REF_DES_ONLY = SET_LINE_NUMBER[SET_LINE_NUMBER.find("Ref"):len(SET_LINE_NUMBER)].replace("RefDes: ","").strip()
        if '- SN: ' in text:
            SN_DUT = text[text.find("- SN: "):text.find(" - Location")].replace("- SN: ","")#read till Location
            LOCATION_DUT = text[text.find("Location:"):text.find("- PN")].replace("Location: ","")
            RESULT_DUT = text[text.find("Result"):len(text)].replace("Result: ","")
            
            serialized_data_refdes = {
                'SN' : [SN_DUT.strip()],
                'LOCATION_FROM_RESULTS':[LOCATION_DUT.strip()],
                'LOCATION_FROM_REFDES' : [GET_LOCATION.strip()],
                'RESULT_DUT':[RESULT_DUT.strip()],     
                'REF_DES':[REF_DES_ONLY.strip()],              
            }
            
            if serialized_data_refdes['SN'] == "":
                pass
            else:
                print(serialized_data_refdes)