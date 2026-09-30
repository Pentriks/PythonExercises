salary = float(input('What is the Employee salary? R$ '))
new = salary + (salary * 15 / 100)

print(f'An employee who earned R${salary:.2f}, with a 15% increase, now receives R${new:.2f}')

