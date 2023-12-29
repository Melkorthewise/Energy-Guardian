from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie
from django.core.serializers.json import DjangoJSONEncoder

# Import non-Django libraries
import mysql.connector
import json
from datetime import datetime, timedelta


"""
 Kilowatt = power, which is the rate that energy is generated or used.
 Kilowatt-Hour = energy, which is the rate that we use fuel over a specific period.

 P(W) = U(V) * I(A)
 E(kWh) = (P(W) * t(s)) / 1000
"""

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="energy_guardian",
    port=3306,
)

mycursor = mydb.cursor()

def usage(user, device, period):
    # Sorteren op datum waar die kijkt naar de meegegeven periode
    mycursor.execute("select wattage.DeviceID, Volt, ampere, pulldatetime from wattage join device on wattage.DeviceID = device.DeviceID where UserID = '{}' and pulldatetime >= NOW() - INTERVAL 1 {};".format(user, period))

    data = mycursor.fetchall()

    # print("Data:", type(data), data, "\n")

    total_energy = 0

    if data != []:
        _, voltage, current, first_timestamp = data[0]
        prev_timestamp = first_timestamp

        for entry in data[1:]:
            _, voltage, current, timestamp = entry

            # Convert timestamp to datetime object (if not already)
            timestamp_datetime = timestamp if isinstance(timestamp, datetime) else datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')

            # Calculate time difference since the previous timestamp
            time_difference = timestamp_datetime - prev_timestamp
            time_seconds = max(time_difference.total_seconds(), 0) # Ensure non-negative time difference

            # Calculate energy for this interval
            power_w = voltage * current
            energy_wh = power_w * (time_seconds / 3600)

            # Accumulate total energy
            total_energy += energy_wh

            # Update the previous timestamp for the next iteration
            prev_timestamp = timestamp_datetime

    total_energy /= 1000

    total_energy = round(total_energy, 2)

    return total_energy


def chart(user, device, period):

    mycursor.execute("select wattage.DeviceID, volt, ampere, pulldatetime from wattage join device on wattage.DeviceID = device.DeviceID where UserID = '{}' and pulldatetime >= NOW() - INTERVAL 1 {};".format(user, period))
    data = mycursor.fetchall()

    # print("Data:", type(data), data, "\n")

    time = []
    value = []

    for x in data:
        # print(x, "\n")
        
        (Device, Voltage, Current, Pulldatetime) = x

        power_w = Voltage * Current
        # energy_wh = power_w * (time_seconds / 3600)

        #Pulldatetime = [x.strftime('%Y-%m-%dT%H:%M:%S')]

        date = Pulldatetime.strftime("%Y-%m-%d %H:%M:%S")

        time.append(date)
        value.append(power_w)
    
    return time, value

def device_status(user):
    
    mycursor.execute("select wattage.DeviceID, volt, ampere, pulldatetime from wattage join device on wattage.DeviceID = device.DeviceID where UserID = '{}' and pulldatetime >= NOW() - INTERVAL 5 MINUTE;".format(user))
    data = mycursor.fetchall()

    if data == []:
        data = False
    else:
        data = True

    return data