# Import Django libraries

# Import non-Django libraries
from coolname import generate_slug

import mysql.connector
import serial
import time

# Import other python files

class PicoReader:
    def __init__(self, port='COM4', baudrate=9600):
        self.serial_port = serial.Serial(port, baudrate, timeout=1)

        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="toor",
            database="energy_guardian"
        )

    def read_data(self):
        try:
            data = self.serial_port.readline().decode('utf-8').strip()

            return data
            
        except serial.SerialException as e:
            print(f"Error reading from serial port: {e}")
            return None 
        
    def register(self, number, UserID):
        print(number)
        He = self.mydb.cursor()
        try:      
            thinking = True

            while thinking:
                slug = generate_slug(2)
                # Check if the slug already exists in the database
                He.execute("SELECT COUNT(*) FROM device WHERE Name_Device = %s", (slug,))
                count = He.fetchone()[0]

                if count == 0:
                    name = slug
                    thinking = False

            sql = "INSERT INTO device (DeviceID, UserID, Name_Device) VALUES (%s, %s, %s)"

            val = (number, UserID, name)

            try:
                He.execute(sql, val)
                self.mydb.commit()
                print(f"{name} set in Database with DeviceID: {number}. From the user with UserID: {UserID}.")
                
            except mysql.connector.Error as err:
                if err.errno == 1062:
                    print(f"Device with DeviceID {number} already exists.")
                else:
                    print(f"Error: {err}")
            finally:
                He.close()
            
        except serial.SerialException as e:
            print(f"Error reading from serial port: {e}")
            return None 
        
        
    def send_signal(self, data):
        try:
            # Send data to the Pico over the serial connection
            self.serial_port.write(data.encode('utf-8'))

            # print(f"{type(data)} {data}")
        except serial.SerialException as e:
            print(f"Error sending data to serial port: {e}")
