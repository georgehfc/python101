import math
# SCRIPT TO SOLVE FOR "SECOND GRADE" EQUATIONS: Ax² + Bx + C = 0
print("### 📊 LET's SOLVE THIS EQUATION 📊 ###")
# SORTING PARAMETERS
a = float(input("Inform value of A: "))
b = float(input("Inform value of B: "))
c = float(input("Inform value of C: "))
# FIND DELTA ∆
delta = b * b - 4 * a * c
print(delta)
if delta > 0.0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("For {}x² + {}x + {} = 0 we see values: x1 = {} e x2 = {}".format(a, b, c, x1, x2))
elif delta == 0.0:
    x = (-b + math.sqrt(delta)) / (2 * a)
    print("For {}x² + {}x + {} = 0 we see value: x = {}".format(a, b, c, x))
else:
    print("There are no real values for {}x² + {}x + {} = 0".format(a, b, c))
