#melhorar o desafio 028
from random import randint
computador = randint(0, 10)
acertou = False #para dar contra prova no while
chute = 0 # para fazer somatório
while not acertou:
    jogador = int(input('QUAL SEU CHUTE ENTRE 0 E 10? '))
    chute += 1
    if chute == computador:
        acertou = True
    else:
        if chute < computador:
            print('MAIS... tente novamente: ')
        elif chute > computador:
            print('MENOS...tente novamente')
print('VOCÊ ACERTOU COM {} TENTATIVAS'.format(chute))
