# THIS SCRIPT RECEIVES TRAVELLED DISTANCE AND ELAPSED TIME
# IN ORDER TO CALCULATE THE AVG SPEED
print("### 🤖 BEEP 🤖 ###")
print("This is the Avarage Speed Calculador!")
dist = input("Type the distance travelled by the scooter (meters)? ")
time = input("How long (minutes) did the scooter travelled for? ")
av = float(dist) / float(time)
print("The scooter reached {:.1f} m/min".format(av))
