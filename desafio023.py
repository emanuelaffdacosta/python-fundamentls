#faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos dígitos separados. ex: digite um número: 1834 / unidade: 4/
# dezena: 3 / centena: 8 / milhar: 1
numero = int((input('Digite um número: ')))
#utilizando a matemática
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Verificando cada dítigo temos...')
print('A unidade é: {}'.format(u))
print('A dezena é: {}'.format(d))
print('A centena é: {}'.format(c))
print('O milhar é: {}'.format(m))