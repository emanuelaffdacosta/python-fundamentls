#convertendo valores
real = float(input('Quanto você tem na carteira? R$ '))
dolar = real / 5.37
euro = real / 5.98
print('Você tem {:.2f} dólares e {:.2f} euros!!'.format(dolar, euro))
