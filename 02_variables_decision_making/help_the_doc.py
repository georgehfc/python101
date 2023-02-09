# THIS SCRIPT FINDS STUDENTS ELIGIBLE FOR AN AWESOME TRIP TO SOUTH AMERICA
print("### 🌎✈️✈️✈️ LET's GO TO SOUTH AMERICA ✈️✈️✈️🌎 ###")
# ASKING FOR STUDENT's INFO
mail = input("Type your e-mail: ")
semester_grade = input("Type your grade in the semester: ")
# CONVERTING TO FLOAT
semester_grade = float(semester_grade)
# LOGIC TEST
if semester_grade > 8.5:
    print("Yes! Sending tickets to {}".format(mail))
