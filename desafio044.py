
print('{:^40}'.format('CASA PIO'))
from time import sleep
valor = float(input('Digite o valor do produto: '))
print('''Qual a forma de pagamento ?
[1] DINHEIRO/CHEQUE
[2] À VISTA NO CARTÃO 
[3] EM ATÉ 2X NO CARTÃO
[4] EM 3X OU MAIS NO CARTÃO''')
opção = int(input('Digite uma das opções: '))
print('PROCESSANDO...')
sleep(2)
dinheiro = valor - (valor * (10 / 100))
cart1 = valor - (valor * (5 / 100))
cart2 = valor
cart3 = valor + (valor * (20 / 100))
cart3 = valor + (valor * (20 / 100))
totparc = int(input('Quantas parcelas? '))
parcela = cart2 /totparc
parcela2 = cart3 / totparc
if opção == 1:
    print('O valor de sua compra será {}'.format(dinheiro))
elif opção == 2:
    print('O valor de sua compra será {}'.format(cart1))
elif opção == 3:
    print('Seu pagamento será em {}x SEM JUROS com parcelas de {}'.format(totparc, parcela))
elif opção == 4:
    print('Sua compra será dividia em {}x em {} parcelas, sua compra sairá por R${:.2f}, com juros de 20%'.format(totparc, parcela2, cart3))
else:
    print('OPÇÃO INVÁLIDA, tente novamente!!')
