price = float(input('What is the price of the product? R$ '))
new = price - (price * 5 / 100)

print(f'The product that cost R${price:.2f}, in the promotion with a 5% discount will cost R${new:.2f}')