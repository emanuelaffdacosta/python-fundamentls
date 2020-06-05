#DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM.
# CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0.50 POR KM PARA VIAGENS DE ATÉ 200KM E
# R$0.45 PARA VIAGENS MAIS LONGAS
d = float(input('Digite a distânica de sua viagem: '))
print('Você irá fazer uma viagem de {} Km'.format(d))
from time import sleep
print('Estamos calculando os valores das passagens...')
sleep(2)
if d <= 200:
    preço = d * 0.50
    print('Sua viagem de {} Km custará R${:.2f}'.format(d, preço))
else:
    preço2 = d * 0.45
    print('Sua viagem {} Km custará R${:.2f}'.format(d, preço2))
