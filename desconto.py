#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
pre = float(input('Qual o preço do produto? R$'))
desconto = pre - (pre * 5/100)
#preço - 5%
print('Este produto está com 5% de desconto, seu valor final será de {:.2f}!!'.format(desconto))
