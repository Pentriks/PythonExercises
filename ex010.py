wallet = eval(input("How much money is in your wallet? R$"))

dolar = wallet / 5.15

print("With R${:.2f} you can buy US${:.2f}".format(wallet, dolar))