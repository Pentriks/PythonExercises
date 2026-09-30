from math import hypot

# Input data
co = float(input('Length of the opposite side: '))
ca = float(input('Length of the adjacent side: '))

# Direct calculation using hypot()
hi = hypot(co, ca)

# Formatted output
print(f'The hypotenuse will measure {hi:.2f}')