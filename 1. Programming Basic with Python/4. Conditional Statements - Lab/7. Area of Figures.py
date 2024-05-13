import math

type_of_figure = str(input())

if type_of_figure == 'square':
    strana = float(input())
    area_of_square = strana * strana
    rounded_value_of_square = round(area_of_square, 3)
    print(f'{rounded_value_of_square:.3f}')
if type_of_figure == 'rectangle':
    side1 = float(input())
    side2 = float(input())
    area_of_rectangle = side1 * side2
    rounded_value_of_rectangle = round(area_of_rectangle, 3)
    print(f'{rounded_value_of_rectangle:.3f}')
if type_of_figure == 'circle':
    radius = float(input())
    area_of_circle = math.pi * radius ** 2
    rounded_area_of_circle = round(area_of_circle, 3)
    print(f'{rounded_area_of_circle:.3f}')
if type_of_figure == 'triangle':
    side1 = float(input())
    side2 = float(input())
    area_of_triangle = (side1 * side2) / 2
    rounded_area_of_rectangle = round(area_of_triangle, 3)
    print(f'{rounded_area_of_rectangle:.3f}')
