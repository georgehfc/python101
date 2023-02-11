# A SCRIPT THAT WON'T LET USER GO UNTIL '42' IS TYPED
# PRACTICING THE WHILE
print("### 🐟 THE ANSWER TO EVERYTHING 🐠 ###")
answer = ""
while answer != "42":
    answer = input("Answer to the Ultimate Question of Life, the Universe, and Everything: ")

print("Congratulations, you are a geek!")

# NOW WE LOOK FOR EVEN NUMBERS
print("### 2️⃣ EVEN NUMBERS 2️⃣ ###")
number = 1
while number % 2 == 1:
    number = int(input("Looking for even number. Have you seen one? "))
print("You made it!")
