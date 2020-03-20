#requires pyserial,colorama
import sys
import time
#imports for serial
import serial.tools.list_ports, serial 
import io
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
VENDOR_ID = "1FC9"
PRODUCT_ID = "009E"


#search in serial.tools for the following data and match it with the user given data
def getSerialPort():
    for port in list(serial.tools.list_ports.comports()):
        if "USB VID:PID=%s:%s" % (VENDOR_ID, PRODUCT_ID) in port[2]:
            return port[0]

#Opening the serialport automatticly using the getSerialport() function.
def StartTest():
    #Opening serial port DUT with following settings 115200,None,8,1
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.parity = serial.PARITY_NONE
    ser.bytesize = serial.EIGHTBITS
    ser.stopbits = serial.STOPBITS_ONE
    print("baudrate set to: %d" % ser.baudrate)
    #connect with COM
    ser.port = '%s' % getSerialPort()
    print("Opened port: %s" % ser.port)
    #Open com and flush bus
    ser.open()
    ser.flush()
    #Opening serial port 254 with following settings 115200,None,8,1
    ser1 = serial.Serial()
    ser1.baudrate = 115200
    ser1.parity = serial.PARITY_NONE
    ser1.bytesize = serial.EIGHTBITS
    ser1.stopbits = serial.STOPBITS_ONE
    ser1.port = "COM254"
    ser1.open()
    ser1.flush()

    ############# Start command
    buffer = ser.read(10)
    print("Response DUT: " + buffer.decode('utf-8'))
    ser.flush()
    sendbuff = '[enabletest]\r\n'
    ser.write(sendbuff.encode('utf-8'))
    buffer = ser.readline()
    print("Response DUT: " + buffer.decode('utf-8'))
    ser.flush()
    ############## End
    ############## Start Test command
    sendbuff = '[gauge]\r\n'
    ser.write(sendbuff.encode('utf-8'))
    buffer = ser.readline()
    ser.flush() #added extra flush for this test
    print("Response DUT: " + buffer.decode('utf-8'))
    buffer = ser.readline()
    ser.flush()
    ############## End Test Command
    print("Response DUT: " + buffer.decode('utf-8'))
    ser1.write("GAUGE:".encode('utf-8'))
    ser1.write(buffer)
    ser.flush()
    ser1.close()
    ser.close()

if __name__ == "__main__":
    StartTest()