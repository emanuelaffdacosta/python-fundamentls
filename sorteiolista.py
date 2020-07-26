# mesmo profe do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
from random import shuffle
a = str(input('Digite o primeiro nome: '))
b = str(input('Digite o segundo nome: '))
c = str(input('Digite o terceiro nome: '))
d = str(input('Digite o quarto nome: '))
lista = [a, b, c, d]
o1 = shuffle(lista)
#shuffle é a função aleatória
print(lista)
'''o2 = random.choice(lista)
o3 = random.choice(lista)
o4 = random.choice(lista)'''
'''print('O segundo a apresentar é {}'.format(ordem))
print('O terceiro a apresentar é {}'.format(ordem))
print('O quarto a apresentar é {}'.format(ordem))'''
