# A SCRIPT THAT CALCULATES THE AVERAGE WEIGHT OF 100 BOXES IN A TRUCK
print("### 🚛 THE TRUCK 🚛 ###")
# THIS BEAUTY STORES THE TOTAL WEIGHT OF BOXES
total_weight = 0.0
# LET'S ITERATE!
for x in range(1, 11):
    # ASKING FOR BOX's WEIGHT EVERY LOOP
    actual_weight = float(input("Type the weight of this box: "))
    total_weight = total_weight + actual_weight
# CALCULATING ARITHMETIC AVG
media = total_weight / 100
# PROMPTING RESULTS!
print("Total weight of the boxes is {:.1f}.".format(total_weight))
print("The average weight of the boxes is {:.1f}.".format(media))
print("#####")
