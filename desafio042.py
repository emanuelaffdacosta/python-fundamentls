# rEFAÇA O DESAFIO 035 DO TRIÂNGULO SERÁ FORMADO:
# EQUILÁTERO
# ISÓCELES
# ESCALENO
a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))
if a < b + c and b < c + a and c < a + b:
    print('O valores podem formar um triângulo', end= ' ')
    if a == b ==c:
        print('Equilátero')
    elif a != b and a != c and b != c:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Os valores disponibilizados NÃO podem formar triângulo!')
