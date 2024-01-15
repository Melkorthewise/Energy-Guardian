# Import Django libraries.

# Import non-Django libraries.
from coolname import generate_slug

import mysql.connector
import serial
import time

# Import other python files.

# Pico related functions
class PicoReader:
    def __init__(self, port='COM4', baudrate=9600):
        try:
            self.serial_port = serial.Serial(port, baudrate, timeout=1)

            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="toor",
                database="energy_guardian"
            )

        except Exception:
            print("Device is not connected.")

    # Read the data from the pico.
    def read_data(self):
        try:
            data = self.serial_port.readline().decode('utf-8').strip()

            return data
            
        except serial.SerialException as e:
            print(f"Error reading from serial port: {e}")
            return None         
        
    # Send a signal to the pico.
    def send_signal(self, data):
        try:
            # Send data to the Pico over the serial connection.
            self.serial_port.write(data.encode('utf-8'))

            print(f"\n{type(data)} {data}")
        except serial.SerialException as e:
            print(f"Error sending data to serial port: {e}")

    # Register the device in the database.
    def register(self, number, UserID):
        He = self.mydb.cursor()
        try:      
            thinking = True

            while thinking:
                slug = generate_slug(2)
                # Check if the slug already exists in the database.
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
                
                return False
                
            except mysql.connector.Error as err:
                if err.errno == 1062:
                    print(f"Device with DeviceID {number} already exists.")

                    return False
                else:
                    print(f"Error: {err}")
            finally:
                He.close()
            
        except serial.SerialException as e:
            print(f"Error reading from serial port: {e}")
            return True 
    
    # Save the calibration data to the database.
    def calibration(self, number):
        Voltage = []
        Current = []

        average_V = 0
        average_A = 0

        x = 0
        
        while x != (5 * 60):
            try:
                data_to_send = "True"
                self.send_signal(data_to_send + "\n")

                data = self.read_data()

                data = data.split(',')

                DeviceID, V, A = data

                Voltage.append(V)
                Current.append(A)

                x += 1
            except ValueError as err:
                print(err)


        numbers = len(Voltage)
        for x in range(len(Voltage)):
            average_V += Voltage[x]

        average_V /= numbers

        numbers = len(Current)
        for x in range(len(Current)):
            average_A += Current[x]

        average_A /= numbers

        print(average_V, average_A)