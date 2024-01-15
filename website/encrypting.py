import bcrypt as B
import socket

class Encrypt:
    def __init__(self):
        pass
    
    
    def bcrypting(self, password):
        
        # Hash the password with the generated salt
        #hashed_password = B.hashpw(password.encode('utf-8'), salt)
        password = password.encode('utf-8')
        hashed_password = B.hashpw(password, B.gensalt())

        print(f"Hashed Password: {hashed_password}")
        
        return hashed_password
    
    def setup(self, password):
        self.password = password
        self.hashed_password = self.bcrypting(self.password)
        print(self.hashed_password)
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", 8000))
        s.send(hashed_password)
        s.close()
        return hashed_password

    def decrypt(self, input, hash):
        check = input.encode('utf-8')
        
        if B.checkpw(check, hash):
            print("succes")
            
        else:
            print("L")
        

# Create an instance of the Encrypt class
enc = Encrypt()

# Your password (change this to the actual password)
password = "dog"

# Bcrypt the password
hashed_password = enc.bcrypting(password)
check = enc.decrypt(password, hashed_password)