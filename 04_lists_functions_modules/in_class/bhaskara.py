def bhaskara(a, b, c):
    delta = b**2 - 4 * a * c
    if delta > 0:
        # duas raízes
        r1 = (-b + delta ** 1/2) / 2 * a
        r2 = (-b - delta ** 1/2) / 2 * a
        return r1, r2
    elif delta == 0:
        # uma raíz
        r1 = -b / 2 * a
        return r1
    else:
        # sem raízes reais
        return None

print(bhaskara(1, 40, 2))   # (378.0, -418.0)
print(bhaskara(2, 4, 2))    # -4.0
print(bhaskara(20, 1, 20))  # None
