casa = float(input('Digite o valor da casa: R$ '))
salário = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * (30 / 100)
print('Para pagar a casa no valor de  {}  em {} anos'.format(casa, anos))
print('Os valores das prestações será de {:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo Concedio')
else:
    print('Empréstimo Negado')
