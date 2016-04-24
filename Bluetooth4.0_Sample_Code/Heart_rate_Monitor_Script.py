
import binascii
import struct
import time
from bluepy.btle import UUID, Peripheral
from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print "inside notification"
        print "Heart rate:", ord(data[1]), "Energy=" ,int(binascii.b2a_hex((data[::-1])[0:2]),16) # This script was tested on ubuntu 14.04
                                                                                                  # To solve the endianess problem reverse the
                                                                                                  # string to find exact value

devices = Scanner()                 # Scanner Object
temp=devices.scan(10)               # Start Scan
try:
    for dev in temp:
        if dev.getScanData()[3][2] == "mr. singh":      # Check for the target BLE device name
            if dev.connectable:
                p = Peripheral(dev.addr, "random")
                p.setDelegate(ScanDelegate())           # Create internal Object of scandelegate class to handle the notifications
except (RuntimeError, TypeError, NameError):
    print "Device not found"
    exit(1)
################### Check for the Services and its characteristics #################
print p.getServices()[0]
print p.getServices()[1]
print p.getServices()[2]
Heart_Rate_Measurement = p.getServiceByUUID(0x180D).getCharacteristics()[0]
Body_Sensor_Location = p.getServiceByUUID(0x180D).getCharacteristics()[1]
Heart_Rate_Control_Point = p.getServiceByUUID(0x180D).getCharacteristics()[2]
print Heart_Rate_Measurement , Heart_Rate_Measurement.uuid              # Print characteristic and its uuid
print Body_Sensor_Location , Body_Sensor_Location.uuid
print Heart_Rate_Control_Point , Heart_Rate_Control_Point.uuid

################## Print the Value ###########################

body_sensor=["not_selected","Chest","Wrist","Finger","Hand","Ear Lobe","Foot"]  # List for body sensor location

try:
    ch = p.getServiceByUUID(0x180D).getCharacteristics()[1]                     # body sensor location characteristics
    print ch
    if (ch.read()):
        print ord(ch.read())                                                    # Print the location
        while True:
            if p.waitForNotifications(1.0):
                # handleNotification() was called
                continue
            print "Waiting..."
            print "Body Sensor Location=", body_sensor[ord(ch.read())]
finally:
    p.disconnect()
