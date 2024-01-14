# This code is written in micropython and is written for the pico.
from machine import Pin, UART
import select
import sys
import time

poll_obj = select.poll() # Create an instance of a polling object
poll_obj.register(sys.stdin, 1) # Register sys.stdin (standard input) for monitoring read events with priority 1

relay = Pin(2, mode=Pin.OUT, value=1) # Pin object for controlling pin 15.

running = False

def read_pzem_data():
    uart = UART(0, baudrate=9600, tx=0, rx=1)
    
    # PZEM-004T command to read voltage and current (register 0 and 1)
    command = bytes([0x01, 0x04, 0x00, 0x00, 0x00, 0x02, 0x71, 0xCB])
    
    # Send the command to PZEM-004T
    uart.write(command)
    
    # Wait for the PZEM-004T to respond
    time.sleep(1)
    
    # Read the response (adjust the number of bytes based on the expected response length)
    response = uart.read(7)
    
    # Parse the response
    if response:
        voltage = response[3] << 8 | response[4]
        current = response[5] << 8 | response[6]
        
        # print(voltage, current)
            
        print ("0, {}, {}".format((voltage * 0.1), (current * 0.001)))
        # print("Voltage:", voltage * 0.1, "V")
        # print("Current:", current * 0.001, "A\n")
    else:
        print("No response from PZEM-004T")

while True:
    if poll_obj.poll(0):
        data = sys.stdin.readline().strip()

        # if data == "True":
            # running = True
        # elif data == "F":
            # running = False
        if data == "off":
            relay.off()
        elif data == "on":
            relay.on()
        
        # if running == True:
            # read_pzem_data()
            
    read_pzem_data()
            
    time.sleep(0.1)
