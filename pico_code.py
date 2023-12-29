# The file is written in micropython
import urequests
import utime

# Fill in the necassary information below
wifi_ssid  = ""
wifi_password = ""

# Change "ip" for the relevant ip address of the django server
server_url = "http://ip:8000/pico"

data_to_send = {"sensor_data": 123}

def connect_to_wifi():
    import network
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(wifi_ssid, wifi_password)
        while not wlan.isconnected():
            pass
        print('Connected to WiFi')
        
#def make_http_request():
#    response = urequests.get(server_url)
#    print('HTTP Response:', response.text)
#    response.close()

connect_to_wifi()

count = 1

while True:
    try:
        response = urequests.post(server_url, json=data_to_send)
        #print("Data sent. Server response:", response.text)
        print("visited: ", count, "time")
        response.close()
        
        count += 1
        
        utime.sleep(30)
        
    except Exception as e:
        print("Error:", str(e))
        utime.sleep(1)