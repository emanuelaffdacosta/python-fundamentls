#Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
# ex: Ana Maria de Souza primeiro = Ana  e ultimo = Souza
n = str(input('Digite um nome completo: ')).title().strip()
nome = n.split()
print('O primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
