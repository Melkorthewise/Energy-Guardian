import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="toor",
    database="energy_guardians",
    port=3306,
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM login")


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'energy_guardian',
#         'USER': 'root',
#         'PASSWORD': 'toor',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     }
# }