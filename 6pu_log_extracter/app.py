import argparse
import os
import fileinput
import linecache
from tarfile import FIFOTYPE


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




FIFO_ARRAY_REFDES = []
with fileinput.input([args.file]) as logfile:
    for text in logfile:
        text.strip()
        if 'TEST FAILURE Failure reason' in text:
            GET_LOCATION = text[text.find("L"):text.find("S")].strip()
            GET_CURRENT_LINE_NUMBER = logfile.filelineno()
            SET_LINE_NUMBER = linecache.getline(args.file, (GET_CURRENT_LINE_NUMBER+1)).strip()
            REF_DES = SET_LINE_NUMBER[SET_LINE_NUMBER.find("Ref"):len(SET_LINE_NUMBER)].replace("RefDes: ","").strip()
            if 'U' in REF_DES:
                FIFO_ARRAY_REFDES.append(REF_DES)
        if '- SN: ' in text:
            SN_DUT = text[text.find("- SN: "):text.find(" - Location")].replace("- SN: ","")#read till Location
            LOCATION_DUT = text[text.find("Location:"):text.find("- PN")].replace("Location: ","")
            RESULT_DUT = text[text.find("Result"):len(text)].replace("Result: ","")
            
            serialized_data_results = {
                'SN' : [SN_DUT.strip()],
                'LOCATION':[LOCATION_DUT.strip()],
                'RESULT_DUT':[RESULT_DUT.strip()],                
            }
            serialized_data_refdes = {
                'LOCATION' : [GET_LOCATION.strip()],
                'REF_DES':[REF_DES.strip()],              
            } 
            #Only print if we have data in SN.
            if serialized_data_results['SN'] == "":
                pass
            else:
                if serialized_data_results["LOCATION"] == serialized_data_results["LOCATION"]:
                    serialized_combined_data = {
                        'SN' : [SN_DUT.strip()],
                        'LOCATION':[LOCATION_DUT.strip()],
                        'RESULT_DUT':[RESULT_DUT.strip()],     
                        'REF_DES':[REF_DES.strip()],      
                    }
                    print(serialized_combined_data)
                else:
                    pass