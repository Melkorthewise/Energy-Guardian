import mysql.connector
from website.encrypting import Encrypt
import bcrypt as B
import os
import time
from coolname import generate_slug

from .pico import *
        
class connecter:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="toor",
            database="energy_guardian"
        )
    
    def login(self, username, password): 
        check = "SELECT Password FROM users WHERE Email_Address = %s"
        values = (username,)

        try:
            self.cursor = self.mydb.cursor()
            self.cursor.execute("SELECT Password FROM users WHERE Email_Address = %s", username)

            result = self.cursor.fetchone()
            print(result)

            if result:
                print("RESULT")
                input_password = password.encode('utf-8')

                if B.checkpw(input_password, result[0]):
                    print("MATCH")
                    return True

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            self.cursor.close()
            self.mydb.close() 
            self.cursor.execute(check, values)

        return False

    def signUp(self, email, firstName, lastName, password):
        inDataBase = False
        data = self.mydb.cursor()
        He = self.mydb.cursor()
        
        symbols = 0
        for letter in firstName:
            symbols +=1
        
        if symbols > 255:
            return "toLongFirst"
        
        symbols = 0
        for letter in lastName:
            symbols += 1
        
        if symbols > 255:
            return "toLongLast"
        
        symbols = 0
        for letters in email:
            symbols += 1
        
        if symbols > 255:
            return "toLongEmail"
        
        symbols = 0
        for letters in password:
            symbols += 1
        
        if symbols < 8:
            return "toShortPassword"
        
        elif symbols > 20:
            return "toLongPassword"
        
        else:
            pass
        
        data.execute("SELECT Email_Address from users")
        
        #Detecteren of het email-address al in gebruik is
        emailaddresses = [row[0] for row in data.fetchall()]
        for data in emailaddresses:
            if data == email:
                return "emailerror"
     
        #email-address niet in gebruik
        else:            
            He.execute("SELECT UserID FROM users")
            userID = [row[0] for row in He.fetchall()]

            old = 0
            setID = 0
            through = True
            
            for id in userID:
                if id == old:
                    old +=1
                else:
                    setID = old
                    through = False
                    break

            if through:
                while setID in userID:
                    setID += 1

            sql = "INSERT INTO users (UserID, Email_Address, FirstName, SecondName, Password) VALUES (%s, %s, %s, %s, %s)"
            password = encr.bcrypting(password)
            
            
            val = (setID, email, firstName, lastName, password)

            try:
                He.execute(sql, val)
                self.mydb.commit()
                print(f"{email} set in Database with UserID: {setID}")

            except mysql.connector.Error as err:
                if err.errno == 1062:
                    print(f"User with UserID {setID} already exists.")
                else:
                    print(f"Error: {err}")

connector_instance = connecter()
encr = Encrypt()