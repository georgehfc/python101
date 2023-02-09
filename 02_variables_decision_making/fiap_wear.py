# FIAP Wear is a virtual stand that sells custom clothes of the brand
# This month it's the store's birthday and a coupom allows 10% off of your cart
print("### 🧢 FIAP WEAR 🧢 ###")
total_shop = input("Please inform us the total ($): ")
coupom = input("Type the discount coupom: ")

if coupom.upper() == "HAPPYB10":
    total_shop = float(total_shop) * 0.9
else:
    total_shop = float(total_shop)
    print("INVALID COUPOM!")

print("The total is ${:.1f}".format(total_shop))
