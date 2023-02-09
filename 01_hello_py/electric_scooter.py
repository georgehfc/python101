# coding: utf-8
# SCRIPT TO CALCULATE AVG SPEED OF SCOOTERS IN SÃO PAULO
print("### 🛴 ELECTRIC SCOOTER 🛴 ###")
print("This script calculates the average speed of a scooter")
dist = input("Type the travelled distance (kilometers): ")
time = input("How long did it take the scooter to stop (minutes)? ")
avg_speed = float(dist) / float(time)
print("The scooter reached {} m/min".format(avg_speed))
