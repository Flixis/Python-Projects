# !/usr/bin/python

# Import QRCode from pyqrcode 
import pyqrcode
from pyqrcode import QRCode
# colour libary
import sys
from colorama import Fore, Back, Style, init, AnsiToWin32
# needed for proper printing in Windows CMD
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
#import for OS commands
import os
import platform
#import for argparse
import argparse



parser = argparse.ArgumentParser(description='Example: QR.py 1 Testing')
parser.add_argument("-T","--Type",help="Example: Test string.",required=False,default="")
parser.add_argument("-V","--Value",help="Example: Test string.",required=False,default="")
args = parser.parse_args()


#Version and OS check
SystemOS = platform.system()
VersionOS = platform.release()
Version = "1.0.0"




 
# Check to see if input is numerical only, used for QRnumerical and start of APP.
def inputnumber(number):
    while True:
        try:
            userInput = int(input(number))
        except ValueError:
            print("Not a numerical value!")
            continue
        else:
            return userInput
            break

#QRcode with numerical value only
def QRnumerical():
    print(Fore.RED + "Creating QR with numerical value only!" + Fore.RESET, file=stream)
    serial = inputnumber("SerialNumber:")
    # Generate QR code , we make the serialqr var global for debug access when program crashes.
    global serialqr 
    serialqr = pyqrcode.create(serial)  
    # Create the QR code with the following settings and output to serial.svg
    print("Creating QRCode with SerialNumber %d" % serial)
    serialqr.svg("Serial.svg", scale = 8, background="white", module_color="black")

#QRcode where anything goes
def QRany():
    print(Fore.RED + "Creating QR with any value/string" + Fore.RESET, file=stream)
    message = ""
    message = input("String to encode:%s " % message)
    # Generate QR code , we make the qr var global for debug access when program crashes.
    global qr 
    qr = pyqrcode.create(message)  
    # Create the QR code with the following settings and output to serial.svg
    print("Creating QRCode with %s" % message)
    qr.svg("QR.svg", scale = 8, background="white", module_color="black")

class MyException(Exception):
    pass

#Start code
if __name__ == "__main__":
    #selection area:
    print(Fore.LIGHTYELLOW_EX + "QRCode generator V%s\n\r" % Version + "Running on %s %s" % (SystemOS, VersionOS) + Fore.RESET , file=stream)
    print("Please choose what kind of QRcode you want to create")
    print("1:Any Value")
    print("2:Numerical only")

    #Make sure selection is interger otherwise error
    try:
        selection = inputnumber("")
        

        if selection == 1:
            #QR with any string
            QRany()
            #Open .svg with default app, windows only?
            if SystemOS == "Windows":
                os.popen("QR.svg")
            elif SystemOS == "Linux":
                os.popen("display QR.svg")
            else:
                print("")
                print(Fore.RED + "PROGRAM CRASHED!", file=stream)
                print("---------------------------")
                print("Debug:")
                print(Fore.GREEN + "Module options: %r" % qr + Fore.RESET,file=stream)
                raise MyException("Couldn't match OS in order to display QRCode.")
        else:
            #QR with numerical only
            QRnumerical()
            #Open .svg with default app, windows only?
            if SystemOS == "Windows":
                os.popen("Serial.svg")
            elif SystemOS == "Linux":
                os.popen("display Serial.svg")
            else:
                print("")
                print(Fore.RED + "PROGRAM CRASHED!", file=stream)
                print("---------------------------")
                print("Debug:")
                print(Fore.GREEN + "Module options: %r" % serialqr + Fore.RESET,file=stream)
                raise MyException("Couldn't match OS in order to display QRCode.")
    except ValueError:
                print("")
                print(Fore.RED + "PROGRAM CRASHED!", file=stream)
                print("---------------------------")
                print("Debug:\n\r")
                raise Exception
