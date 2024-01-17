# Manual of the Energy Guardian Model C

For a project on THUAS we have created the Energy Guardian Model C. But let's start from the beginning, we will start with the choosing of a SDG, a Sustainable Development Goal.

## Table of Contents
- [The Challenge - Fase 1](#the-challenge---fase-1)
    * [The Solution](#the-solution)
    * [Functional Design](#functional-design)
        + [List of Functional Demands](#list-of-functional-demands)
        + [Motivation & Explanation Functional Design](#motivation--explanation-functional-design)
    
- [Energy Guardian Model C](#energy-guardian-model-c)

- [Server](#server)
    * [Frontend](#frontend)
        + [Javascript](#javascript)
            - [Settings](#settings)
            - [Update](#update)
            - [Plotter](#plotter)

    * [Backend](#backend)
        + [Navigation](#navigation)
        + [Views](#views)
        + [Database Connection](#database-connection)
        + [Sign Up](#sign-up)
            - [Encryption](#encryption)
        + [Login](#login)
            - [Decryption](#decryption)
            - [SQL Injection](#sql-injection)
        + [Error Codes (Detection)](#error-codes-detection)
        + [Settings](#settings-1)
            - [Changing Password](#changing-password)
            - [Deleting Account](#deleting-account)

- [Microcontrollers](#microcontrollers)
    * [Raspberry Pi Pico](#raspberry-pi-pico)
    * [Micro:bit](#microbit)

- [Database](#database)
    * [Tables](#tables)
    * [Saving](#saving)

- [Hardware](#hardware)
    * [Components](#components)
    * [Connections](#connections)

- [Setup](#setup)

## The Challenge - Fase 1

There were 17 goals that we could choose from. We chose number 7, **Affordable and Clean Energy**. We chose this one, because we thaught that this was the most promising way for us. We also think it is important that everyone can live a sustainable life in their own way.

> Ensure access to affordable, reliable, sustainable and modern energy for all. (UN, 2023)

What we learned after doing some research is that there are still 675 milion people without electricity. We also learned that on average a houshold of 4, in the Netherlands, that live in a terraced or corner house consumes 2.500 kWh. And a detached house uses up to 3.300 kWh. (Tess, 2023)

That is why we want to create a solution that helps people to optimize their energy consumption at home an thus save valuable energy.

### The Solution

Our project has the goal to minimize the power consumption of housholds and electrical appliances. We want to do this with the help from a microcontroller. Our solution is to integrate this technology in a standard power strip or coupling piece, so that it will be turned off automatically when the connected device is below a certain Wattage. This would significantly improve energy efficiency and minimize unnecessary consumption.

To achieve this, there are multiple components that we will need. We are considering using a Arduino or a Micro:bit, together with sensors that are able to accurately measure electricity consumption. These sensors will most likely monitor the voltage and amperage of the power consumption of connected devices, which would allow the wattage to be calculated.

An essential part of our project is the development of a web application. This application will be used as a interface where users can communicate with the microcontroller in the power strip. Through this app the users can not only get information about their power consumption, but also they could make adjustments to save energy more efficient. There would also be a page where you could set timers of when the device should turn of the connected device. This gives the users the flexibility to make their power consumption fit to their standards.

Through this integrated approach, we want to help people be more efficient with their energy consumption and at the same time reduce their ecological footprint. Reducing unnecessary power consumption not only benefits individuals, but also contributes to a greener and more sustainable future for us all.

### Functional Design

#### List of Functional Demands

Here is a list of demands that we had in mind:
- There must be a server to save the information.
- Has to be a (web)application.
- Must be using a microcontroller.
- It has to be as small as possible.
- It must be compact.
- It has to be something we can present.
- Should be aimed to TVs

#### Motivation & Explanation Functional Design

> Here we explain why we chose all the demands and how we have prioritized it.

As first we have the server, this will add everything that we receive or transmit together. Without a server we cannot transmit, receive or display any information.

Then we have the (web)webapplication. This one is necessary, because it makes communiction possible. So, can we send commands to the microcontroller. To control this we will need a database, so that the server can get the data from here.

The most important part of the product, is the microcontroller. This is the key to automatically disabling the connected device. This the reason that there will be something happening, for example disabling a TV. This shall send all the data from the sensor to the database.

From now there will be some things that are less important for us. We want the device to be as little as possible. With making it as compact as possible, we can make the product very clear and beautiful. That will not be looking like a simple microcontroller.

It would also be fun when we will be presentating it, that it would be beautiful and fun to do so. We want to make the product as presentable as possible. We want to do this by really making something that we will be able to hold. 

Even though we are not sure about this, we probably want to focus this solution on a TV. This is the easiest to visualize for now. This can always be changed. We also want to make it possible to connect it to multiple devices later.

# Energy Guardian Model C

The end product exists of 3 parts. We have the server, database and hardware parts. The server part will be about the connections between the other layers and about the frontend. The database part will be about how we structured the database and why, there also will be a little about saving the data. The hardware part will be about the different components and how these works. It will also be about how it works in a total.

# Server

We have created a server with Python, we used the django library for this. We then created the pages with HTML and CSS. The server connected everything that we have.

## Frontend

With creating the frontend we used HTML and CSS, as mentioned above. We also used some Javascript when we needed it, more on that later.

### Javascript

#### ***Settings:***
>*To change your password, there is next to some Python code also some Javascript code used. If you press the submit button after filling in the password fields, comes there first a verification question, a confirm function, if you really want to change your password. Because of csfr_tokens, that is in the HTML code, will there after the conformation of changing the passwords the `views.py` be loaded. Through the function settings will the `settings.py` be activated to change the password.*
>
> *To delete your account we will be again using the crsf_tokens. Only this time we changed the submit changed to a yes or no button, with a 6 symbolic code, via the prompt functie, which will be randomly generated. When the entered code is incorrect, there will appear an error. This will say that the codes are not the same. Because of this there will not be made a connection with the `views.py` file, which then does not calls the delete function in the `settings.py` file.*

#### ***Update:***
> *On the update page you can find the latest updates. The updates are read from a textfile and then showed upon the page. The updates from the file get seperated with a '\n', an enter, so that all the updates will be viewed clean under each other.*

#### ***Plotter:***
> *Because we want the user to see there power usage, we are using a plotter. This plotter shows the power against the date and time. We are showing this plotter with Chartjs. The data gets pulled from the database, it shows only the data from the last hour.*

## Backend

With creating the backend we used Python. As mentioned before we used the Django module for creating the server. We did this, so that our microcontroller, the Raspberry Pi Pico, could connect to it. This would make it possible to transmit and receive the data through the wifi connection. But for one reason or the other did this not work in our school, so we changed the connection temporarly to USB.

### Navigation

Because there are multiple pages on a website, we have to distingish between these pages. But most important is that when we go to a certain address, the right page will show up. That is why there is a file called `urls.py`. This file makes the right address goes to the right function, which in time shows the right page.

This page has multiple paths that will look a lot like this path here below. You have the function path, were you first say the address of the page. Then you say which function from the 'views.py' file corresponds with this address. As last you have a name, this is there to make sure there is no conflicts between the pages.

```
path(route, view, name=None)
```

### Views

You also have a file called `views.py`. Here you write all the code needed for the website, that still is needed for the backend. When the backend is done, you can use a return statement to show a template, which shows the frontend.

For example we have this function for a home page. You will have the path: `path('home', views.home, name="home")`. When you start the server, it now has an address called home, you can visit it on `127.0.0.1:8000/home`. But it probably give an error, because there is no function in `views.py` called home. If you create a function that will display a HTML file, you first have to import render from django.shortcuts. But then you will create a function that will look like this:

```
def home(request):
    return render(request, 'home.html')
```

After this you can add more and more python code, just how you like it. But do not use time.sleep() for a long period. The page will then freeze up and maybe will unload it, because it takes so long.


### Database Connection

We wanted to have a database with our website, but the build in models from Django did not do it for us. So we imported mysql.connector and builded our database in the mysql workbench.

When we want to connect to the database we will have some code that looks like this:
```
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="toor",
    database="energy_guardian",
    port=3306,
)

mycursor = connection.cursor()
```

So, the host is a localhost with the port 3306. There is an user in the workbench called 'root', with the password 'toor'. The database for our project is called 'energy_guardian'.

After this you can use MYSQL queries just how you like it, but with python. Here are examples on how to use the select, insert and update queries.

- ` mycursor.execute("SELECT ... FROM ...") `
- ` mycursor.execute("INSERT INTO (..., ..., ...) VALUES (..., ..., ...) ") `, with insers you have to commit the query like this: `connection.commit()`.
- ` mycrusor.execute("UPDATE ... SET ... = ...") `, which you also have to commit.

### Sign Up

For the functions like the one needed for the sign up we have made a file called `connect.py`. Here there is a function called signUp where it gets the variables called email, firstName, lastName and password.

It then checks if the email is already used for an account, if so it gives an notice otherwise it continues. It then figures out which UserID to give to the person, it does this by selecting all the used UserID's. It then checks if there is any room otherwise it just uses the next last UserID + 1. It then encrypts the password, where you can find more about under 'Encrytion'. If everything is alright it then inserts the user into the users table in our database. You are then signed up and are ready to use the website.

#### Encryption

To make sure our users data is save, we encrypt the passwords. Here we use the library called Bcrypt. We get the password from the sign up page. Then we compare the two passwords with each other. If these match up, we make a connection with the database. When that has happened we translate the string with the password to utf-8, so that bcrypt can hash the password. The hashed password then gets send from `encryptie.py` to `connect.py`, which then continues with saving the user.

### Login

When the user trys to login, we need the email and password. That were filled in when creating the account. 

#### Decryption

We get the password in a string format en change this to utf-8, so that we can compare these with the hashed password from the database. We also check if the right email is filled in. To compare the filled in password with the hashed password, we use the build in funcion from bcrypt, bcrypt.checkpw().

#### SQL Injection

Because we first check if the two passwords are the same in Python code, instead of SQL-code is it not possible to do a SQL-injection. The checkpw() function first hashes the password and then start to look if they are the samen, is it not possible to do a SQL-injection.

### Error Codes (Detection)

If an error occurs during logging in or creating an account, because the password entered does not belong to the account when logging in or if the passwords are not the same or the email address is already in use, or the first or the second name is to long. The code will detect this. We will then send error messages with if_tokens to the relevant HTML file when re-rendering the page.

### Settings

With the settings page, you can change your password and delete your account.

#### Changing Password

To make it possible to change your password, we read both the input fields and compare these two passwords with each other. If these are not the same, than the password does not get updated in the database. When the passwords are identical to each other, there will be made a connection with the database and the password gets updated.

#### Deleting Account

To delete you account, you push the 'Delete Account' button. This will then delete your account.

## Microcontrollers

When the server starts, there are two background processes that will start. These will keep going until the server is stopped. One is for the Raspberry Pi Pico and the other one is for the remote, which in our case is the Micro:bit.

### Raspberry Pi Pico

When the proces for the Pico starts, there will be a while loop running that will not be stopped. In this loop, there will first be made a connection with the database, for in the case data must be saved to the database. Then it starts to read the data from the serial connection, through the USB cable. The data the gets picked up, will be change this, so that it can be saved in the database with the table Wattage.

#### Registering

To make it possible to register your device, we have made a page where you can do this. Here you can fill in the unique ID of the device, which then gets saved in the database with the ID of the user and a random generated name.

### Micro:bit

For the Micro:bit there will also be a loop started, which then first looks for the Micro:bit. For testing reasons it looks now for a specific Micro:bit, but later this can change. If this one is found, it will connect with the Micro:bit and will start to read the output of the buttons. When button A is pressed, it will send a signal to the Pico to turn off the TV. When button B is pressed it will send a signal that will turn on the TV.

# Database

So as mentioned before, we have made a database in the MYSQL Workbench. This made it easier to create and use the database, then the Django models database.

The database has a function to save the data, also it has to make it easy to get data from it. The data that gets saved in the database are login data from the users, device data and power usage data. 

## Tables

We have created four tables, a users table, a device table, a calibration table and a wattage table. But first we had to create the database itself. We did this with: ` CREATE DATABASE Energy_Guardian; ` then we used ` USE Energy_Guardian ` so that it creates the tables in the right database.

The users table will save the users credentials, so that he/her can login when wanted. The table looks like this:

> | UserID | Email_Address        | FirstName | SecondName | Password          |
> | :----: | -------------------- | --------- | ---------- | ----------------- |
> |   0    | forexample@gmail.com | John      | Doe        | Hashed_Password   |
> |   1    | forexample@yahoo.com | Doe       | John       | Hashed_Password   |

We got the email address and password, so that the user can login and the name just for customization purposes, the user does not need to fill these in. The UserID we add, to easely filter the accounts.

We used this code to create the table:

```
CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    Email_Address VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Password VARCHAR(255) NOT NULL,
);
```

We did the same for the other tables. For the table devices we needed a DeviceID, to identify the device. We also needed a UserID, this is a foreign key that references the users table. We need this so that the data gets displayed with the right person. And the Name_Device is there, so that we can show a name instead of the DeviceID.

For the calibration table we need the Device_mode, so that we know if the device is turned on or off. We then have the DeviceID, so that we can monitor the right data. There is then just the Average_Voltage and Average_Ampere, so that it can reference this to look if the device must be shutdown.

With the Wattage table we have a WattageID, we added this later because it was not that easy to edit the data. We then have the DeviceID, to identify which data is from which device. We save then the most important data, that is the Volt and the Ampere. Which is logical, because we need that for our product to work. We then have a pulldatetime, so that we can show the data in a chart. Which shows that wattage, against the date + time.

# Hardware



## Components

For the making of our device we used the following components:
- Raspberry Pi Pico
- PZEM-004T (multimeter sensor)
- Relay
- Wall outlet
- Junction box
- Cables

### Circuit

![Energy Guardian Circuit](website\static\Pico.png)

We used the Raspberry Pi Pico as the microcontroller. It controlled the sensor and the relay. 

## Connections





















# Setup