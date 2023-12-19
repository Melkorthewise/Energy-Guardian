import mysql.connector

class connecter:
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="energy_guardian"
        )
    
    def login(self, username, password):   
        self.__init__()
        data = self.mydb.cursor()

        check = "SELECT Email_Address, Password FROM users WHERE Email_Address = %s AND Password = %s"
        values = (username, password)
        data.execute(check, values)

        myresult = data.fetchall()

        if myresult:
            return True
        else:
            return False

    def signUp(self, email, firstName, lastName, password):
        data = self.mydb.cursor()
        
        data.execute("SELECT UserID FROM users")
        userID = [row[0] for row in data.fetchall()]

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
        val = (setID, email, firstName, lastName, password)

        try:
            data.execute(sql, val)
            self.mydb.commit()
        except mysql.connector.Error as err:
            if err.errno == 1062:
                print(f"User with UserID {setID} already exists.")
            else:
                print(f"Error: {err}")



connector_instance = connecter()