
import serial
import datetime
from mintsXU4 import mintsSensorReader as mSR
from mintsXU4 import mintsDefinitions as mD
import time
import serial
from collections import OrderedDict

portIn    =  "/dev/ttyUSB2"
baudRate  =  4800

def main():

    ser = serial.Serial(
    port= portIn,\
    baudrate=baudRate,\
    parity  =serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=0)

    delta  = 5
    print("connected to: " + ser.portstr)

    line = []
    while True:
        # try:
        for c in ser.read():
            line.append(chr(c))
            print(line)
            if chr(c) == '\n':
                dataString     = (''.join(line)).replace("\r\n","")
                print(line)
                print("-=----")
                dateTime  = datetime.datetime.now()
                print(dataString)
                print(dateTime)
                line = []
                break;
        # except:
        #     print("Incomplete String Read")
            # line = []
                    
    ser.close()



if __name__ == "__main__":
   main()


