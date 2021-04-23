#requires pyserial,colorama
import sys
import time
import argparse
#imports for serial
import serial.tools.list_ports, serial 
# colour libary
from colorama import Fore, Back, Style, init, AnsiToWin32
# needed for proper printing in Windows CMD
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream



#----Arg parsing----#
parser = argparse.ArgumentParser(description='Example: app_Serial.py -v 0403 -p 6001')
parser.add_argument("-l","--LIST",metavar='',help="List all devices.")
parser.add_argument("-v","--VID",metavar='',help="Vendor ID.")
parser.add_argument("-p","--PID",metavar='',help="Product ID.")
args = parser.parse_args() 


if args.LIST:
    print('not implemented yet.')
    exit(1)

print(Fore.YELLOW + "\nLooking for device with VID %s and PID %s" % (args.VID,args.PID) + Fore.RESET, file=stream)

#Print all serial devices and its requested items.
for port in serial.tools.list_ports.comports():
        portpid = ""
        portvid = ""
        if port.vid is None:
            print("")
        else:
            portvid = hex(port.vid)
            portpid = hex(port.pid)
        print(port.description, port.device, portvid, portpid)

print("\n")

VENDOR_ID = args.VID
PRODUCT_ID = args.PID

#search in serial.tools for the following data and match it with the user given data.
def getSerialPort():
    for port in list(serial.tools.list_ports.comports()):
        if "USB VID:PID=%s:%s" % (VENDOR_ID, PRODUCT_ID) in port[2]:
            return port[0]

if __name__ == "__main__":
    SerialPort = getSerialPort()
    if SerialPort:
        print(Fore.GREEN + "Match on %s.\n" % SerialPort + Fore.RESET, file=stream)
    else:
        print(Fore.RED +"No compatible Port found. Aborting." + Fore.RESET, file=stream)
        time.sleep(1.5)
        exit(1)