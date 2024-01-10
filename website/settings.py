import mysql.connector
from django.views.decorators.csrf import ensure_csrf_cookie
from website.encrypting import Encrypt

class Settings:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="toor",
        database="energy_guardian"
        )
        
        self.cursor = self.mydb.cursor()
    
    def changePassword(self, userID, password):   
        self.__init__()
        newPassword = Encrypt().bcrypting(password)
            	        
        query = "UPDATE users SET Password = %s WHERE userID = %s"
        values = (newPassword, userID)
        self.cursor.execute(query, values)
        self.mydb.commit()
    
    def deleteAccount(self, userID):
        self.__init__()
        query = "DELETE FROM users WHERE userID = %s"
        values = (userID,)
        self.cursor.execute(query, values)
        self.mydb.commit()