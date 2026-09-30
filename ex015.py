# Input data
days = int(input('How many days was the car rented for? '))
km = float(input('How many km driven? '))

# Business logic: $60 per day and $0.15 per km
total = (days * 60) + (km * 0.15)

# Formatted output using f-string
print(f'The total amount to pay is ${total:.2f}')