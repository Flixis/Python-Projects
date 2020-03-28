#requires pyserial,colorama
import sys
import time
#imports for serial
import serial.tools.list_ports, serial 
# colour libary
from colorama import Fore, Back, Style, init, AnsiToWin32
# needed for proper printing in Windows CMD
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream


#Print all serial devices and its requested items, note vid and pid print in interger not hex cba to fix it
print(Fore.RED + "Note that VID and PID are printed as an interger! VID -> 3 , PID -> 4" + Fore.RESET, file=stream)
print(Fore.MAGENTA + "                            VID   PID        " + Fore.RESET,file=stream)
for port in serial.tools.list_ports.comports():
        print(port.description, port.device, port.vid, port.pid)

print("\n")

# Hardcoded versions
#VID & PID Must be a HEX value
VENDOR_ID = "0403"
PRODUCT_ID = "6001"


#search in serial.tools for the following data and match it with the user given data
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