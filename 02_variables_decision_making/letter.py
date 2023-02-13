# SCRIPT THAT WON'T DISMISS UNTIL LETTER IS TYPED
# PRACTICING THE WHILE
# MADE IN CLASS 9Fev
print("### 🔤 FIND THE LETTER 🔤 ###")
letter = input("Input a letter: ")

while letter != 'x':
    print("Wrong letter...")
    letter = input("Type another letter: ")

print("Finally! You found '{}'.".format(letter))

# while True:
#     letter = input("Input a letter: ")
#     if letter == 'x':
#         break
#     print("Wrong letter...")

# DICTIONARY (TUPLA)
print("##########")
sheet = ('George', 33, 'Lisbon', 'Portugal')
print(f'Name: {sheet[0]}')
print(f'Age: {sheet[1]}')
sheet = [{
    "Name": "George",
    "Surname": "Chaves",
    "test!"
    "Age": 33,
    "City": "Lisbon",
    "Country": "Portugal"
}]
# print(sheet[0]["Name"])
for person in sheet:
    for key, value in person.items():           # .items() IS BUILT-IN
            print(f"{key}   •   {value}")
    print("*" * 10)
print(type(person))
