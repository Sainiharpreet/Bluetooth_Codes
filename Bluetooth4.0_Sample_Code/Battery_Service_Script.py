import binascii
import struct
import time
from bluepy.btle import UUID, Peripheral
from bluepy.btle import Scanner, DefaultDelegate

# Wrapper around DefaultDelegate class to handle the Notifications
class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print "inside notification"
        print "Handle=" ,cHandle, "Battery level=", ord(data)

devices = Scanner()                                     # Scanner Object
temp=devices.scan(10)                                   # Start Scan

for dev in temp:
    if dev.getScanData()[3][2] == "mr. singh":          # Check for the target BLE device name
        if dev.connectable:
            p = Peripheral(dev.addr, "random")          # Connect to the Device
            p.setDelegate(ScanDelegate())               # Create internal Object of scandelegate class to handle the notifications

try:
    ch = p.getServiceByUUID(0x180F).getCharacteristics()[0] # get battery level characteristic for battery Service
    print ch
    if (ch.read()):
        print ord(ch.read())                                # Read the characteristic Value
        while True:
            if p.waitForNotifications(1.0):
                # handleNotification() was called
                continue
            print "Waiting..."
finally:
    p.disconnect()
