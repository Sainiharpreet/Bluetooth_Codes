
import bluetooth

target_name = "honey singh"
target_address = None

nearby_devices = bluetooth.discover_devices(8,True,False)   # Find all nearby Devices
print nearby_devices
target_address =nearby_devices

for bdaddr in nearby_devices:                               # scan nearby_devices list for our target bluetooth device
    print bluetooth.lookup_name( bdaddr )
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print "found target bluetooth device with address ", target_address
    print bluetooth.find_service(uuid=None, address="target_address")   # Print the target device services
else:
    print "could not find target bluetooth device nearby"

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )   # Open Socket
server_sock.bind(("",bluetooth.PORT_ANY))                   # Bind Socket
server_sock.listen(1)                                       # Listen to 1 incomming connections. This is simiar to socket programming

port = server_sock.getsockname()[1]

uuid = "1101"

bluetooth.advertise_service( server_sock, "SampleServer",   # Advertise Host SPP as it was not included in Host service record earlier
                   service_id = uuid,
                   service_classes = [ uuid, bluetooth.SERIAL_PORT_CLASS ],
                   profiles = [ bluetooth.SERIAL_PORT_PROFILE ],
                    )

print "Waiting for connection on RFCOMM channel %d" % port

client_info = server_sock.accept()                        # Accept the connection
print "Accepted connection from ", client_info

try:
    while True:
        data = client_sock.recv(1024)                       # recieve the incoming bytes
        if len(data) == 0: break
        print "received [%s]" % data
        client_sock.send(data)                              # Echo the recieved bytes
except IOError:
    pass

print "disconnected"

server_sock.close()                                         # Close the Socket
print "all done"