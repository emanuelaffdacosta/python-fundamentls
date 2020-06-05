#um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa
# que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
# import random
from random import choice
a = str(input('Digite o primeiro nome: '))
b = str(input('Digite o segundo nome: '))
c = str(input('Digite o terceiro nome: '))
d = str(input('Digite o quarto nome: '))
#lista em python deve vir entre colchetes
lista = [a, b, c, d]
#sorteado = random.choice(lista)
sorteado = choice(lista)
print('O aluno escolhido foi {}'.format(sorteado))