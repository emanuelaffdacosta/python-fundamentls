# CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE SE É PAR OU IMPAR
num = int(input('Digite um valor inteiro: '))
resu = num % 2
if resu == 0:
    print('É PAR')
else:
    print('É ÍMPAR!!')
