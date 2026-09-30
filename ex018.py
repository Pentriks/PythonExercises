from math import radians, sin, cos, tan

# Input data (angle in degrees)
angle = float(input('Enter the angle you want: '))

# Necessary conversion: Degrees to Radians
rad = radians(angle)

# Calculation of Sine, Cosine, and Tangent
sine = sin(rad)
cosine = cos(rad)
tangent = tan(rad)

# Formatted output (2 decimal places)
print(f'The angle of {angle}° has a SINE of {sine:.2f}')
print(f'The angle of {angle}° has a COSINE of {cosine:.2f}')
print(f'The angle of {angle}° has a TANGENT of {tangent:.2f}')