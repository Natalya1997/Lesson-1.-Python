import math

def square(side):
    return math.ceil(side * side)

size_side = float(input('Введите размер стороны: '))
print(f'Площадь квадрата: {square(size_side)}')