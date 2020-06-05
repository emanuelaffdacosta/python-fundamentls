#faça um programa que leia um ângulo qualquer e mostre na tela o vaalor do seno, cosseno e tangente desse angulo
# import math
from math import radians, sin, cos, tan, asin
angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
'''print(f'O valor do seno é {seno}, cosseno é {cosseno} e tangent é {tangente}')'''
print('O valor do seno é: {:.2f}'.format(seno))
print('O valor do cosseno é: {:.2f}'.format(cosseno))
print('O valor da tangente é: {:.2f}'.format(tangente))


'''nesse caso precisou transformar em radianos para depois solucionar o seno, cosseno e tangente'''