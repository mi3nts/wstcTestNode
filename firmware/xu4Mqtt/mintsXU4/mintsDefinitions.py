
from getmac import get_mac_address
import serial.tools.list_ports

# Added March 1sr 2023: for ports with same names and PID 

def findPortV2(inStr,lenStr):
    print(inStr)
    print(lenStr)
    ports    = list(serial.tools.list_ports.comports())
    outPorts =  []
    for p in ports:
        currentPort = str(p[1])
        print(len(currentPort))
        if(currentPort.find(inStr)>=0 and len(currentPort)==lenStr):
            outPorts.append(str(p[0]).split(" ")[0])
    return(outPorts)

print(findPortV2("USB-Serial Controller",21))

def findPort(find):
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        currentPort = str(p)
        if(currentPort.endswith(find)):
            return(currentPort.split(" ")[0])

def findIPSPorts():
    ports = list(serial.tools.list_ports.comports())
    ipsPorts = []
    for p in ports:
        currentPort = str(p[2])
        if(currentPort.find("PID=10C4")>=0):
            ipsPorts.append(str(p[0]).split(" ")[0])
    return ipsPorts
  
def findAirmarPort():
    ports = list(serial.tools.list_ports.comports())
    ozonePort = []
    for p in ports:
        currentPort = str(p[2])
        if(currentPort.find("PID=067B")>=0):
            ozonePort.append(str(p[0]).split(" ")[0])
    return ozonePort
  

def findMacAddress():
    macAddress= get_mac_address(interface="eth0")
    if (macAddress!= None):
        return macAddress.replace(":","")

    macAddress= get_mac_address(interface="docker0")
    if (macAddress!= None):
        return macAddress.replace(":","")

    macAddress= get_mac_address(interface="enp1s0")
    if (macAddress!= None):
        return macAddress.replace(":","")

    macAddress= get_mac_address(interface="wlan0")
    if (macAddress!= None):
        return macAddress.replace(":","")

    return "xxxxxxxx"



dataFolderReference       = "/home/teamlary/mintsData/reference"
dataFolderMQTTReference   = "/home/teamlary/mintsData/referenceMQTT"
dataFolder                = "/home/teamlary/mintsData/raw"
dataFolderMQTT            = "/home/teamlary/mintsData/rawMQTT"


macAddress            = "001e0610c0e4"

latestDisplayOn       = False
latestOn              = False

airmarPorts           = findPortV2("USB-Serial Controller D",23)
rg15Ports             = findPortV2("USB-Serial Controller",21)
canareePorts          = findPortV2("Canaree PM",10)

ipsPorts              = ["/dev/ttyS1"]


# For MQTT 
mqttOn                = True
mqttCredentialsFile   = 'mintsXU4/credentials.yml'
mqttBroker            = "mqtt.circ.utdallas.edu"
mqttPort              =  8883  # Secure port


gpsPort               = findPort("GPS/GNSS Receiver")


if __name__ == "__main__":
    # the following code is for debugging
    # to make sure everything is working run python3 mintsDefinitions.py 
    print("Mac Address                : {0}".format(macAddress))
    print("Data Folder Reference      : {0}".format(dataFolderReference))
    print("Data Folder Raw            : {0}".format(dataFolder))
    print("Latest On                  : {0}".format(latestOn))
    print("MQTT On                    : {0}".format(mqttOn))
    print("MQTT Credentials File      : {0}".format(mqttCredentialsFile))
    print("MQTT Broker and Port       : {0}, {1}".format(mqttOn,mqttPort))


    #-------------------------------------------#
    print("RG15 Ports :")
    for dev in rg15Ports:
        print("\t{0}".format(dev))
    #-------------------------------------------#
    print("IPS Ports :")
    for dev in ipsPorts:
        print("\t{0}".format(dev))
    #-------------------------------------------#
    print("Canaree Ports :")
    for dev in canareePorts:
        print("\t{0}".format(dev))