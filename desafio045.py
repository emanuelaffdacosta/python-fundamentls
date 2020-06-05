from random import randint
from time import sleep
item = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
print('''ESCOLHA UMA OPÇÃO:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
'''sleep(1)'''
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PON!!')
print('~-'*11)
print('Computador jogou {}'.format(item[computador]))
print('Jogador jogou {}'.format(item[jogador]))
print('~-'*11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador GANHOU')
    elif jogador == 2:
        print('Computador GANHOU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('Computador GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador GANHOU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('Jogador GANHOU')
    elif jogador == 1:
        print('Computador GANHOU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
