a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
#nesse caso só deverá ter if, sugestão: fixar um item como o menor, para fazer as
# verificações de cada um dos tres valores
#verificando os menores
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando os maiores
maior = a
if b > a and b > a:
    maior = b
if c > a and c > a:
    maior = c
print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))


