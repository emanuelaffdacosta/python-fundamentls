# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR PENSAR EM UM NÚMERO INTEIRO ENTRE 0 E 5
# E PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU
from random import randint
computador = randint(0, 5) #Faz o computador "PENSAR"
print('^~' * 30)
print('Te desafio a adivinhar o número entre 0 a 5, que estou pensando')
print('^~' * 30)
numero = int(input('Digite o valor de pensei: '))
from time import sleep
print('PROCESSANDO...')
sleep(3)
if numero == computador:
    print('Aee, você acertou, o valor que pensei foi {}'.format(computador))
else:
    print('HAHAHA você errou, o número que pensei foi {}! Quer jogar de novo?'.format(computador))
