#ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO E CALCULE O VALOR DO SEU
# AUMENTO; PARA SALÁRIOS SUPERIORES A R$1.250,00, CALCULE UM AUMENTO DE 10%
#PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%
salário = float(input('Digite o valor do seu salário R$ '))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Olá seu salário de {}, teve um reajuste para {}'.format(salário, novo))


