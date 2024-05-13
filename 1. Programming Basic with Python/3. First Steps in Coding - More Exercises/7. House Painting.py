
height_as_x = float(input())
length_as_y = float(input())
roof_height_as_h = float(input())

# paint consumption:
green_paint_consumption = 3.4
red_paint_consumption = 4.3

# non-paint area:
door = 1
window = 2

# door and windows size
door_size = 1.2*2
window_size = 1.5*1.5

# calculating non-paint area
non_paint_door_size = door_size
non_paint_windows_size = window_size

# finding wall area:
wall1 = (height_as_x * height_as_x) - non_paint_door_size
wall2 = height_as_x * height_as_x
wall3 = (height_as_x * length_as_y) - non_paint_windows_size
wall4 = (height_as_x * length_as_y) - non_paint_windows_size

# finding roof area:
triangle_sides = 2    # has 2 sides
rectangle_sides = 2   # has 2 sides
one_side_triangle = ((height_as_x * roof_height_as_h) / 2)
one_side_rectangle = (height_as_x * length_as_y)
all_roof_area = (one_side_triangle*triangle_sides) + (one_side_rectangle*rectangle_sides)

# needed paint
needed_paint_for_the_walls = (wall1+wall2+wall3+wall4) / green_paint_consumption
needed_paint_fro_the_roof = all_roof_area / red_paint_consumption

print(f'{needed_paint_for_the_walls:.2f}')
print(f'{needed_paint_fro_the_roof:.2f}')
