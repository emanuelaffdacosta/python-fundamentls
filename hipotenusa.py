# faça um programa que leia o comprimento do cateto adjacente de um triangulo retangulo. calcule e mostre o comprimento da hipotenusa
from math import hypot
#ou pode ser feito assim import math e p/ resposta colocar math. e o respectiva função)
# import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
# hipotenusa² = oposto² + adjacente²
'''hipotenusa = (co ** 2 + ca ** 2) ** (1/2)'''
# hipotenusa = co **2 + ca ** 2
hipotenusa = hypot(co, ca)
print('O valor do cateto oposto {} mais o cateto adjacente {} é igual a hipotenusa {:.2f}'.format(co, ca, hipotenusa))

