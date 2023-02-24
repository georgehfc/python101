grades = []

option = -1

while option!=4:
    print("1 - Input grade\n2 - Display grades\n3 - Calculate average\n4 - Sair")

    option = int(input("Pick an option: "))

    if option==1:
        grades.append(float(input("Type a grade: ")))

    elif option==2:
        print("# Grades!")
        for grade in grades:
            print(f'# {grade}')

    elif option==3:
        print("# Average!")
        print(f'# {sum(grades)/len(grades):.2f}')
