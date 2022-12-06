import math

def sqrt_mas(mas):
    for i in range(len(mas)):
        mas[i] = int(math.sqrt(abs(mas[i])))

    return mas