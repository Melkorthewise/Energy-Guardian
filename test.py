import serial
import serial.tools.list_ports

def find_device_port(target_device_description):
    available_ports = list(serial.tools.list_ports.comports())
    
    matching_ports = [port for port, desc, hwid in available_ports if target_device_description in desc]
    
    if not matching_ports:
        print(f"No {target_device_description} found.")
        return None
    else:
        return matching_ports[0]

def connect_to_device(port):
    try:
        ser = serial.Serial(port, baudrate=9600, timeout=1)  # Adjust baudrate and timeout as needed
        return ser
    except serial.SerialException as e:
        print(f"Error connecting to {port}: {e}")
        return None

if __name__ == "__main__":
    target_device_description = "USB Serial Device"  # Modify based on your ESP8266 description
    
    esp8266_port = find_device_port(target_device_description)
    
    if esp8266_port:
        print(f"{target_device_description} found on port: {esp8266_port}")
        esp8266_serial = connect_to_device(esp8266_port)
        if esp8266_serial:
            print("Connected to ESP8266.")
            # Perform operations with the ESP8266 serial connection here
    else:
        print("No ESP8266 found.")
    
    # Repeat the process for the Pico or other devices if needed
    # pico_port = find_device_port("Pico's Description")
    # if pico_port:
    #     print("Pico found on port:", pico_port)
    #     pico_serial = connect_to_device(pico_port)
    #     if pico_serial:
    #         print("Connected to Pico.")
            # Perform operations with the Pico serial connection here
