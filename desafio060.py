# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE O SEU FATORIAL
'''from math import factorial
num = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(num)
print('o fatorial de  {} é {}'.format(num, f))'''
num = int(input('Digite um número: '))
contador = num
f = 1   #fator nulo da multiplicação e divisão / na soma e subtração é o zero
print('Calculando {}! = '.format(num), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    if contador > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    #print(' x ' if contador > 1 else ' = ', end='') posso fazer como acima e tb como esse.
    f *= contador
    contador -= 1
print('{}'.format(f))
