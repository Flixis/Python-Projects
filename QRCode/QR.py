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
#import for CMD commands
import os
import platform

#Version
SystemOS = platform.system()
VersionOS = platform.release()
Version = "1.0.0"


 
# Check for QRnumerical to confirm int usage 
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
    # Generate QR code 
    serialqr = pyqrcode.create(serial)  
    # Create the QR code with the following settings and output to serial.svg
    print("Creating QRCode with SerialNumber %d" % serial)
    serialqr.svg("Serial.svg", scale = 8, background="white", module_color="black")
    #debug code goes here:
    print(Fore.GREEN + "Module options: %r" % serialqr + Fore.RESET,file=stream)

#QRcode where anything goes
def QRany():
    print(Fore.RED + "Creating QR with any value/string" + Fore.RESET, file=stream)
    message = ""
    message = input("String to encode:%s " % message)
    # Generate QR code 
    qr = pyqrcode.create(message)  
    # Create the QR code with the following settings and output to serial.svg
    print("Creating QRCode with %s" % message)
    qr.svg("QR.svg", scale = 8, background="white", module_color="black")
    #debug code goes here:
    print(Fore.GREEN + "Module options: %r" % qr + Fore.RESET,file=stream)

#Start code
if __name__ == "__main__":
    #selection area:
    print(Fore.LIGHTYELLOW_EX + "QRCode generator V%s\n\r" % Version + "Running on %s %s" % (SystemOS, VersionOS) + Fore.RESET , file=stream)
    print("Please choose what kind of QRcode you want to create")
    print("1:Any Value")
    print("2:Numerical only")
    #Make sure selection is interger otherwise error
    try:
        selection = None
        selection = int(input())
        if selection != 1:
            QRnumerical()
            #Open .svg with default app, windows only?
            if SystemOS == "Windows":
                os.popen("Serial.svg")
            else:
                 os.popen("display Serial.svg")
        else:
            QRany()
            #Open .svg with default app, windows only?
            if SystemOS == "Windows":
                os.popen("QR.svg")
            else:
                os.popen("display QR.svg")
    except:
        print(Fore.RED + "I don't know how you did it, but you really fucked it this time." + Fore.RESET, file=stream)
