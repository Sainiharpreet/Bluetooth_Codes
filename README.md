# Bluetooth Codes

        This Repo contains the sample Bluetooth code written in Python. All the sample codes are tested on Ubuntu 14.04.
    1- The Basic Bluetooth Pairing code is witten using Bluez Dbus Interface and methods. It is in Bluez_dbus folder.
       D-feet was used for monitoring and debugging dbus. The code was tested for pairing android phone with ubuntu Desktop.
    2- Serial Port Profile Sample code was devloped using pybluez. Pybluez is the wrapper class around bluez api. An echo
       message code is developed and tested with ubuntu and android phone. Android App Unwired Lite was installed on phone.
       This example code can be used to develop the application which allows you to send commands and receive data between 
       Bluetooth serial devices connected to microcontrollers such as Arduino, PIC, Raspberry PI, etc.
    3- For bluetooth 4.0 bluepy was used. This is wrapper class around bluez for communication with BLE devices. Communication 
       using 2 profiles is tested viz:- a) Battery Service Profile b) Heart rate measurement Profile. There are two seperate 
       scripts for both profiles.
