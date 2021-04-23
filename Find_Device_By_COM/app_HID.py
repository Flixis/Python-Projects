from pywinusb import hid
import sys
# colour libary
from colorama import Fore, Back, Style, init, AnsiToWin32
# needed for proper printing in Windows CMD
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream

#Vars for VID and PID
VID = input('Enter VID: ')#0x04D8
PID = input('Enter PID: ')#0x00DF

#convert from String to HEX
VID = int(VID, 16)
PID = int(PID, 16)

#Debug to check if its actually HEX
#print(hex(VID))
#print(hex(PID))

#Get all HID devices, useful for finding VID AND PID ID
#filter = hid.HidDeviceFilter()

# or particular vendor_id, product_id range (Current device is PIC24Dev board)
filter = hid.HidDeviceFilter(vendor_id=VID, product_id=PID)

#give hid_device the device(s) it found under the filter
hid_device  = filter.get_devices()

#print(hid_device )
if hid_device :
    print("Looking for device(s) with VID:0x%X and PID:0x%X" %(VID,PID))
    print(Fore.GREEN + "Found %d matching hid devices:"% len(hid_device ), file=stream)
    #Get the first device in the list and select it
    device = hid_device[0]
    device.open()
    print(Fore.YELLOW,hid_device,file=stream)
    print(Fore.GREEN + 'Opened device succesfully', file=stream)
    device.close()
    print(Fore.CYAN + 'Closed device succesfully', file=stream)
else:
    print(Fore.RED + 'Found No HID devices!!',file=stream)
input()