# SCHOOL'S OWN SPORTS TEAM IS RECRUITING
print("### ⚽️🏀🏈 JOIN THE SPORTS TEAM ⚽️🏀🏈 ###")
stu_id = input("Insert your Student's ID: ")
stu_age = input("Insert your age: ")

if int(stu_age) >= 18:
    print("Your participation was authorized, student #{}".format(stu_id))
    print("###### SUCCESS! ######")
    print("More info will be sent to your school mail")
else:
    parents_auth = input("Do you have your parent's authorization? Y-YES or N-NO: ")
    if parents_auth == 'Y':
        print("Your participation was authorized, student #{}".format(stu_id))
        print("###### SUCCESS! ######")
        print("More info will be sent to your school mail")
    else:
        print("Sorry, your participation was denied because of your age")
        print("∆∆∆ Exiting... ∆∆∆")
