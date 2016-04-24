import glib
import dbus
from dbus.mainloop.glib import DBusGMainLoop

dbus_loop = DBusGMainLoop(set_as_default=True)

ml = glib.MainLoop()

bus = dbus.SystemBus()              #org.bluez deamon is on system bus. Hence create object of class SystemBus

manager = dbus.Interface(bus.get_object('org.bluez', '/'), 'org.bluez.Manager')
print manager.ListAdapters()        # print all adapter
print manager.DefaultAdapter()      # print default adapter
def_interface = dbus.Interface(bus.get_object('org.bluez', manager.DefaultAdapter()), 'org.bluez.Adapter')

print def_interface.GetProperties() # print properties of default interface

### The below function will be called whenever DeviceFound Signal will be emmited ##

def device_found(addr, value):
    print 'Found:', addr
    print "Descriptor:", value
    if value == 'mr. singh':            # Name of our target BT device
        temp=def_interface.CreatePairedDevice(addr, manager.DefaultAdapter(), "NoInputNoOutput")
    print temp
    def_interface.StopDiscovery()
    ml.quit()

def_interface.connect_to_signal('DeviceFound', device_found)    # register for the Signal
def_interface.StartDiscovery()      # Call the method of Default interface
ml.run()                            # Runt the event loop