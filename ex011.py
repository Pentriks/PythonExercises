width = float(input('Enter the wall width!'))
height = float(input('Enter the wall height!'))
area = width * height
paint = area / 2

print(f'Its wall has the dimension of {width} x {height} and its area {area:.2f}m2.')
print(f'To paint this wall, you will need {paint:.2f}l of paint.')
