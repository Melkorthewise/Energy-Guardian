#!/usr/bin/env python3
# Code from: https://forums.raspberrypi.com/viewtopic.php?t=301414#p1809106
import time
import os

serial_connected = 0
if os.path.exists('COM4') == True:
    import serial
    ser = serial.Serial('COM4', 115200)
    serial_connected = 1
    time.sleep(1)

while True:
    time.sleep(2)
    for x in range (0,5):
        command = str(x) + "\n"
        ser.write(bytes(command.encode('ascii')))
        if ser.inWaiting() > 0:
            pico_data = ser.readline()
            pico_data = pico_data.decode("utf-8","ignore")
            print (pico_data[:-2])  