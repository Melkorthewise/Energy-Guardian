# Import Django libraries.

# Import non-Django libraries.
from coolname import generate_slug
from threading import Thread

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

            # print(f"\n{type(data)} {data}")
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
    def calibration(self, number, mode):
        Voltage = []
        Current = []

        Average_V = 0
        Average_C = 0
        
        def loop():
            x = 0

            self.send_signal("on" + "\n")

            time.sleep(5)

            while x <= 20:
                self.send_signal("True" + "\n")

                try:
                    try:
                        data = self.read_data()

                        # print(f"Calibration Data({x}): {type(data)}, {data}")

                        data = data.split(',')

                        _, data_v, data_c = data

                        Voltage.append(data_v)
                        Current.append(data_c)

                        x += 1
                        
                    except AttributeError:
                        time.sleep(0.1)
                except ValueError:
                    print("Error:", type(data), data)

                time.sleep(1)
        
        thread = Thread(target=loop, daemon=True)
        thread.start()

        thread.join()

        # print(Voltage)
        # print(Current)

        for x in range(len(Voltage)):
            Average_V += float(Voltage[x])
            Average_C += float(Current[x])

        Average_V /= len(Voltage)
        Average_C /= len(Current)

        # print(Average_V, Average_C)

        mycursor = self.mydb.cursor()

        # Check if there is already something saved in the database
        sql = "SELECT * FROM calibration WHERE DeviceID = %s and Device_mode = %s;"
        mycursor.execute(sql, (number, mode,))

        data = mycursor.fetchall()

        if data == []:
            sql = "INSERT INTO calibration (Device_mode, DeviceID, Average_Voltage, Average_Ampere) VALUES (%s, %s, %s, %s)"
            
            try:
                mycursor.execute(sql, (mode, number, Average_V, Average_C,))
                self.mydb.commit()
            except mysql.connector.Error as err:
                if err.errno == 1062:
                    print(f"Device with DeviceID {number} already exists.")

                    return False
                else:
                    print(f"Error: {err}")
            finally:
                mycursor.close()
        else:
            sql = "UPDATE calibration SET Average_Voltage = %s, Average_Ampere = %s WHERE Device_mode = %s and DeviceID = %s;"
            try:
                mycursor.execute(sql, (Average_V, Average_C, mode, number))
                self.mydb.commit()
            except mysql.connector.Error as err:
                if err.errno == 1062:
                    print(f"Device with DeviceID {number} already exists.")

                    return False
                else:
                    print(f"Error: {err}")
            finally:
                mycursor.close()