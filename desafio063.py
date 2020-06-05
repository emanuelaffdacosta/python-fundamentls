#SEQUÊNCIA DE FIBONACCI (escreva um programa que leia um número n
# inteiro qualquer e mostre
# na tela os n primeiros elementos de uma
# sequência de Fibonacci.
'''0  1  1  2  3  5  8  13 21 34
            t1 t2 t3'''
print('~õ~' * 10)
print('SÉRIE DE FIBONACCI')
print('~õ~' * 10)
termos = int(input('Quantos termos você quer ver?  '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
contador = 3 # vai começar em 3 pq os outros termos já foram definidos
while contador <= termos:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1
print(' => fim!')
