# FEITO PELO PROFESSOR
def bhaskara(a, b, c):
    delta = (b**2) - (4 * a * c)

    if delta > 0:
        raiz_1 = (b * (-1) + delta ** 1/2) / 2 * a
        raiz_2 = (b * (-1) - delta ** 1/2) / 2 * a
        return raiz_1, raiz_2
    elif delta == 0:
        raiz_1 = b * (-1) / 2 * a
        return raiz_1
    else:
        return None


print(bhaskara(1, 40, 2))
print(bhaskara(2, 4, 2))
print(bhaskara(20, 1, 20))
