import win32com.client
import sys
# colour libary
from colorama import Fore, Back, Style, init, AnsiToWin32
# needed for proper printing in Windows CMD
init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream
# Libary voor WIN32 info

# Warp win32client and look for de right folder en the data that i'm looking for
objSWbemServices = win32com.client.Dispatch(
    "WbemScripting.SWbemLocator").ConnectServer(".", "root\cimv2")
# For loop that looks inside the WIN32 Tabel
for item in objSWbemServices.ExecQuery("SELECT * FROM Win32_PnPEntity"):
    print('-'*60)
    # For loop filters on the following criteria
    for name in ('Availability', 'Description', 'DeviceID', 'HID\VID_046D&PID_C332&MI_01&COL05\7&1798FD2C&0&0004',  'InstallDate', 'Manufacturer', 'Name', 'PNPDeviceID',
                 'Service', 'Status', 'StatusInfo'):
        # If this all checks out, push data to 'a' var
        a = getattr(item, name, None)
        # check if 'a' is not empty en then print
        if a is not None:
           print('%s: %s' % (name, a))

# Red text for CMD en don't let the CMD close
print(Fore.RED + 'Press enter to exit', file=stream)
input()

# Requires: "Pywin32"
# Install Pywin 32 using pip
