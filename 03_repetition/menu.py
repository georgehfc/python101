# A SCRIPT THAT DISPLAYS A MENU
print("### 📕 THE MENU 📕 ###")
# CONTROLLING VARIABLE
control = -1
# WHILE USER DOES NOT TYPE EXIT OPTION (4)
while control != 4:
    print("SUPER DUPER MENU!")
    print("1 - Run option 1")
    print("2 - Run option 2")
    print("3 - Run option 3")
    print("4 - Exit program")
    control = int(input("Inform you option: "))

    # VERIFYING AVAILABLE OPTIONS
    if control == 1:
        print("RUNNING OPTION 1!")
    elif control == 2:
        print("RUNNING OPTION 2!")
    elif control == 3:
        print("RUNNING OPTION 3!")

# LOOP WAS BROKEN!
print("OK! Shutting down the program...")
print("#####")
