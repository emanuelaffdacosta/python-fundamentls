#DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS E DIGA AO USUÁRIO
# SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO
'''Para construir um triângulo é necessário que a medida de
qualquer um dos lados seja menor que a soma das medidas
dos outros dois e maior que o valor absoluto da diferença
entre essas medidas.'''
'''x = (b - c ) < a < b + c
y = (a - c) < b < a + c
z = (a - b) < c < a + b'''
print('~º'*15)
print('Verificador de Triângulos')
print('~º'*15)
a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))
if a < b + c and b < a + c and c < a + b:
    print('Os valores fornecidos formam um triângulo!')
else:
    print('Os valores fornecidos não formam um triangulo!')