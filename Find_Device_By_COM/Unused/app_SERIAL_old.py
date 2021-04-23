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
print(Fore.RED + "Note that VID and PID are printed as an interger! VID -> 3 , PID -> 4 and Serial Number -> 5 \n" + Fore.RESET,file=stream)
print(Fore.MAGENTA + "                            VID   PID     SN " + Fore.RESET,file=stream)
for port in serial.tools.list_ports.comports():
        print(port.description, port.device, port.vid, port.pid, port.serial_number)

print("\n")

# Hardcoded versions
VENDOR_ID = "0403"#input('Enter VID: ')  
PRODUCT_ID = "6001"#input('Enter PID: ') 
#SERIAL_NUMBER = "FT1EIVYQA"

# Input versions
#VENDOR_ID = input('Enter VID: ')
#PRODUCT_ID = input('Enter PID: ')
SERIAL_NUMBER = input('Enter SERIAL_NUMBER: ')

#search in serial.tools for the following data and match it with the user given data
def getSerialPort():
    for port in list(serial.tools.list_ports.comports()):
        if port[2] == "USB VID:PID=%s:%s SER=%s" % (VENDOR_ID, PRODUCT_ID, SERIAL_NUMBER):
            return port[0]    
        #Comments are debug that I refuse to remove
        #Note that I used SNR instead of SER which is what caused me a whole lot of trouble
        #print (port[2])
        #if port[2] == "USB SNR=%s" % (VENDOR_ID): 
        #print("USB VID:PID=%s:%s SER=%s" % (VENDOR_ID, PRODUCT_ID, SERIAL_NUMBER), Fore.RED + "THIS IS THE DATA I SEND, PLEASE BE THE SAME AS THE DATA IT READS!" + Fore.RESET)


#The part that actually loads the damn program
if __name__ == "__main__":
    SerialPort = getSerialPort()
    if SerialPort:
        print(Fore.GREEN + "Serial Number found on %s.\n" % SerialPort + Fore.RESET, file=stream)
        print(Fore.YELLOW + "Press enter to exit.", file=stream)
        input()
    else:
        print(Fore.RED +"No compatible Port found. Aborting." + Fore.RESET, file=stream)
        time.sleep(1.5)
        exit(1)
        #print(Fore.YELLOW + "Press enter to exit.", file=stream)
        #input()