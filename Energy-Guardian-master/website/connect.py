import mysql.connector

class connecter:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="energy_guardian"
        )
    
    def check(self):   
        self.__init__()
        data = self.mydb.cursor()

        data.execute("SELECT Email_Address, Password FROM login")

        myresult = data.fetchall()

        for x in myresult:
            print(x)

    def signUp(self, email, firstName, lastName, password):
        data = self.mydb.cursor()

        data.execute("SELECT MAX(UserID)+1 FROM login")
        result = data.fetchone()

        new_userid = result[0] if result is not None and result[0] is not None else 1

        sql = "INSERT INTO login (UserID, Email_Address, FirstName, SecondName, Password) VALUES (%s, %s, %s, %s, %s)"
        val = (new_userid, email, firstName, lastName, password)
        data.execute(sql, val)
        self.mydb.commit()



connector_instance = connecter()

connector_instance.check()