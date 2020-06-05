#ESCREV UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO. SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO,A MUITA VAI CUSTAR R$7.00 POR CADA KM ACIMA DO LIMITE
vel = float(input('Digite sua velocidade: '))
v = (vel - 80) * 7
from time import sleep
print('Estamos processando seus dados...')
sleep(3)
if vel > 80.00:
    print('Você excedeu o limite de velocidade permitida de 80Km/h!')
    print('O valor de sua multa é de {} reais'.format(v))
else:
    print('Parabéns, Você respeita as leis de trânsito!!')
print('Tenha um Bom dia! Dirija com segurança!!')